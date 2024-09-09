from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

# Open the target webpage
url = 'https://glomacs.com/training-course/advanced-building-information-modeling'
driver.get(url)

# Give the page some time to load
time.sleep(3)

# Define XPaths for sections and course outline
sections_xpath = '//*[@id="outline-wrapper"]/div[1]/div[1]/div[5]'
outline_xpath = '//*[@id="outline-wrapper"]/div[1]/div[1]/div[8]'

# Create a dictionary to hold the data
data = {}

# Fetch Course Details
try:
    sections_element = driver.find_element(By.XPATH, sections_xpath)
    data['Course Details'] = sections_element.text
except Exception as e:
    data['Course Details'] = f"Error: {str(e)}"

# Fetch Course Outline
try:
    outline_element = driver.find_element(By.XPATH, outline_xpath)
    data['Course Outline'] = outline_element.text
except Exception as e:
    data['Course Outline'] = f"Error: {str(e)}"

# Close the driver
driver.quit()

# Convert data to a DataFrame
df = pd.DataFrame(list(data.items()), columns=['Section', 'Content'])

# Save to CSV
df.to_csv('course_details_outline.csv', index=False)
print("Data saved to 'course_details_outline.csv'")
