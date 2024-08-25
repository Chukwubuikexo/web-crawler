#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time
import pandas as pd
from datetime import datetime
import os
#%%
# List of User-Agents to randomize
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0 Safari/537.36",
]

# Select a random User-Agent
user_agent = random.choice(user_agents)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--headless") 

# Set up the Selenium WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Go to the website
driver.get("https://www.carsdirect.com/green-cars/electric?headerChange=true&page=2")

# Wait for the page to fully load
driver.implicitly_wait(10)  # wait 10 seconds

# Find all car listings
cars = driver.find_elements(By.CLASS_NAME, 'ncResultCard')

# Data storage
data = []

# Loop through each car listing and extract name and price
for car in cars:
    try:
        car_name = car.find_element(By.CLASS_NAME, 'desktopTitle').text
        car_price = car.find_element(By.XPATH, ".//span[contains(text(),'Price:')]/following-sibling::span").text
        data.append({
            'car_name': car_name,
            'car_price': car_price,
        })
        time.sleep(random.uniform(3, 7))  # Random delay
    except Exception as e:
        print(f"Encountered an error: {e}. Retrying after a delay...")
        time.sleep(60)  # Wait for 60 seconds before retrying

# Close the browser
driver.quit()

# Define the file path
file_path = 'car_data.csv'

# Create DataFrame
df = pd.DataFrame(data)

# Check if the file exists
file_exists = os.path.isfile(file_path)

# Save data to a CSV file with headers if file does not exist
df.to_csv(file_path, mode='a', header=not file_exists, index=False)

# %%
