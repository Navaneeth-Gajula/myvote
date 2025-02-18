from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get('https://mycutebaby.in/contest/participant/679e77f65b140')

    # Wait for the page to load
    time.sleep(10)

    vote_form = driver.find_element(By.ID, "votefrm_sec")
    print(vote_form.text)

    # Find the button by its ID and click it
    vote_button = driver.find_element(By.ID, 'vote_btn')
    vote_button.click()

    print("Vote button clicked successfully!")
    # after clicking the button wait for 4 seconfs and extract all the content from id votefrm_sec
    time.sleep(4)
    vote_form = driver.find_element(By.ID, "votefrm_sec")
    print(vote_form.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()