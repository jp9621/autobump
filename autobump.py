import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

def automate_browser():
    firefox_options = Options()
    #firefox_options.add_argument("--headless")  # Run Firefox in headless mode (without opening a window)
    driver = webdriver.Firefox(options=firefox_options)
    # Replace DISBOARD BUMP LINK with actual link
    driver.get("DISBOARD BUMP LINK")
    
    # Wait for the page to load (adjust the sleep time if needed)
    time.sleep(15)
    
    # Close the browser window
    # driver.quit()

while True:
    automate_browser()
    # Wait for two hours before repeating (adjust the sleep time if needed)
    time.sleep(15)
