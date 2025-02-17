from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

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
