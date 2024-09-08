from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import jsonlines
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Simplified as per your request

# Open the initial course link
course_url = 'https://glomacs.com/training-courses/executive-development'
driver.get(course_url)
driver.maximize_window()

# Wait for the page to load completely
time.sleep(5)

def scrape_course_data():
    """
    Function to scrape course content and course outline from the current course page.
    Returns a dictionary with course title, content, and outline.
    """
    try:
        # Get course title
        course_title = driver.find_element(By.XPATH, "//h1").text.strip()

        # Extract course content
        course_content = driver.find_element(By.XPATH, "//*[@id='outline-wrapper']/div[1]/div[1]/div[5]").text

        # Extract course outline
        course_outline = driver.find_element(By.XPATH, "//*[@id='outline-wrapper']/div[1]/div[1]/div[8]").text

        # Store the extracted data
        return {
            'Course Title': course_title,
            'Course Content': course_content,
            'Course Outline': course_outline
        }
    except NoSuchElementException as e:
        print(f"Error extracting course data: {e}")
        return None

def click_next_page():
    """
    Function to click the 'Next' button to go to the next page.
    Returns True if it navigated to the next page, False if there are no more pages.
    """
    try:
        # Use an alternative XPath or CSS Selector to ensure correct element is targeted
        next_button = driver.find_element(By.XPATH, "//*[@id='container-content-archive']/div/div[1]/div[4]/div/div/div/ul/li/a[contains(text(),'Next')]")
        driver.execute_script("arguments[0].scrollIntoView();", next_button)  # Scroll to the next button
        time.sleep(2)  # Wait for any dynamic content to load
        next_button.click()
        time.sleep(5)  # Wait for the next page to load
        return True
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f"Error navigating to the next page: {e}")
        return False

# Initialize JSONLines writer
with jsonlines.open('courses_data.jsonl', mode='w') as writer:
    while True:  # Loop through all pages
        # Locate the course list using the provided XPath
        courses = driver.find_elements(By.XPATH, "//*[@id='cl-courses']/div/div/div[2]/h2/a")

        for i in range(len(courses)):
            try:
                # Refresh course elements after navigating back
                courses = driver.find_elements(By.XPATH, "//*[@id='cl-courses']/div/div/div[2]/h2/a")
                
                # Get the course link element
                course_link = courses[i]

                # Use JavaScript to click the link to avoid ElementClickInterceptedException
                driver.execute_script("arguments[0].click();", course_link)
                time.sleep(5)  # Wait for the course page to load

                # Scrape data and write to JSONLines file
                course_data = scrape_course_data()
                if course_data:
                    writer.write(course_data)

                # Go back to the course list page
                driver.back()
                time.sleep(5)  # Wait for the course list page to reload
            except Exception as e:
                print(f"Error processing course {i+1}: {e}")
                driver.back()
                time.sleep(5)  # Ensure back navigation if an error occurs

        # Navigate to the next page
        if not click_next_page():
            break  # Exit the loop if no more pages are found

# Close the browser
driver.quit()
