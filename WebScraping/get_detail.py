from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

# Open the target webpage
url = 'https://glomacs.com/training-course/advanced-building-information-modeling'
driver.get(url)

# Wait until the 'outline-text bg-silver' sections are present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'outline-text'))
)

# Define the section titles to look for
section_titles = {
    'INTRODUCTION': None,
    'Objectives': None,
    'Training Methodology': None,
    'Organisational Impact': None,
    'Personal Impact': None,
    'WHO SHOULD ATTEND?': None
}

# Find all sections under the 'outline-text bg-silver' class
try:
    outline_rows = driver.find_elements(By.CLASS_NAME, 'outline-row')
    for row in outline_rows:
        # Scroll to the element to make sure it is visible
        ActionChains(driver).move_to_element(row).perform()

        # Find the title of the section
        try:
            title_element = row.find_element(By.TAG_NAME, 'h3')
            title = title_element.text.strip()

            # If the title is in the section_titles dictionary, extract the content
            if title in section_titles:
                # Look for content inside the same 'outline-row' div (not inside the h3)
                try:
                    # Look for content inside <p>, <ul>, <div>, or <li>
                    content_elements = row.find_elements(By.XPATH, "./p | ./ul | ./div | ./li")
                    # Combine all texts into a single string
                    content_texts = [el.text.strip() for el in content_elements if el.text.strip()]
                    section_titles[title] = "\n".join(content_texts) if content_texts else None
                except:
                    section_titles[title] = None  # If no content found, set as None
        except Exception as e:
            continue
except Exception as e:
    print(f"Error extracting sections: {e}")

# Extract Course Outline details
course_outline = []

try:
    outline_section = driver.find_element(By.CLASS_NAME, 'outline-text.w-border')
    day_titles = outline_section.find_elements(By.CLASS_NAME, 'day-title')
    day_descriptions = outline_section.find_elements(By.CLASS_NAME, 'day-description')
    
    # Combine each day title and description
    for title, description in zip(day_titles, day_descriptions):
        course_outline.append({
            "Day Title": title.text.strip(),
            "Day Description": description.text.strip()
        })
except Exception as e:
    course_outline = None  # Assign None if the content is not available

# Add Course Outline to the main data dictionary
data = section_titles
data['Course Outline'] = course_outline

# Close the driver
driver.quit()

# Convert data to JSON format
json_data = json.dumps(data, indent=4)

# Save to JSON file
with open('course_details.json', 'w') as f:
    f.write(json_data)

print("Data saved to 'course_details.json'")
