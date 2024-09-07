from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

# Navigate to the GLOMACS website
driver.get('https://glomacs.com/')
driver.maximize_window()  # Maximize the browser window

# Wait for the page to load completely
time.sleep(5)  # Adjust sleep time if needed

# Locate the 'Training Subjects' menu item and click to open the page
training_subjects_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'TRAINING SUBJECTS')]")
training_subjects_menu.click()

# Wait for the new page to load
time.sleep(5)

# Locate all elements with courses using the given XPath
course_elements = driver.find_elements(By.XPATH, "//*[@id='nav-cat-all']//div[contains(@class, 'training-filter')]")

# Initialize an empty list to store course titles and links
courses_list = []

# Extract course titles and links
for element in course_elements:
    # Find the course title
    title_element = element.find_element(By.XPATH, ".//a[@class='cl-item-title-url']/h3")
    course_title = title_element.text.strip()

    # Find the course link
    link_element = element.find_element(By.XPATH, ".//a[@class='cl-item-title-url']")
    course_link = link_element.get_attribute('href')

    # Append the title and link as a tuple to the list
    courses_list.append((course_title, course_link))

# Print the extracted course titles and links
for course in courses_list:
    print(f"Title: {course[0]}, Link: {course[1]}")

# Save the extracted courses to a file
with open('glomacs_courses.txt', 'w') as file:
    for course in courses_list:
        file.write(f"Title: {course[0]}, Link: {course[1]}\n")

# Close the browser
driver.quit()
