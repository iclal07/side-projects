from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Simplified as per your request

# Open the webpage
url = 'https://glomacs.com/training-course/advanced-building-information-modeling'
driver.get(url)

# Give the page some time to load
time.sleep(3)

# Define XPaths for the desired sections
sections = {
    'INTRODUCTION': '//*[@id="a0"]/following-sibling::p',
    'Objectives': '//*[@id="a1"]/following-sibling::ul',
    'Training Methodology': '//*[@id="a2"]/following-sibling::p',
    'Organisational Impact': '//*[@id="a3"]/following-sibling::p',
    'Personal Impact': '//*[@id="a4"]/following-sibling::p',
    'WHO SHOULD ATTEND?': '//*[@id="a5"]/following-sibling::p',
    'Course Outline': '//*[@id="a6"]/following-sibling::ul'
}

# Extract data and store in a dictionary
data = {}

for section, xpath in sections.items():
    try:
        element = driver.find_element(By.XPATH, xpath)
        data[section] = element.text
    except:
        data[section] = "Not found"

# Close the driver
driver.quit()

# Convert data to a DataFrame
df = pd.DataFrame(list(data.items()), columns=['Section', 'Content'])

# Save to CSV
df.to_csv('course_details.csv', index=False)
print("Data saved to 'course_details.csv'")
