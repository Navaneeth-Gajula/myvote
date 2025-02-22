from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set up Chrome options
options = webdriver.ChromeOptions()
# Remove the --headless flag
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Set the User-Agent to mimic a mobile device (e.g., Chrome on Android)
mobile_user_agent = (
    "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36"
)
options.add_argument(f'user-agent={mobile_user_agent}')

# Set mobile emulation options
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": mobile_user_agent,
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# Disable automation flags
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Add additional options to make the browser appear more like a real browser
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-notifications')


driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    '''
})

try:
    # Open the website
    driver.get('https://mycutebaby.in/contest/participant/679e77f65b140')

    # Wait for the page to load
    time.sleep(10)

    # print all text from website not page source
    print(driver.find_element(By.TAG_NAME, 'body').text)

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







