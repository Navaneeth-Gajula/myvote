from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome WebDriver
service = Service("/usr/local/bin/chromedriver")  # Path to ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without UI (for GitHub Actions)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(service=service, options=options)

def click_button():
    driver.get("https://mycutebaby.in/contest/participant/679e77f65b140")  # Replace with target site
    time.sleep(5)
    try:
        button = driver.find_element(By.ID, "vote_btn")  # Update button ID
        button.click()
        print("Button clicked!")
    except Exception as e:
        print("Error:", e)

click_button()
driver.quit()
