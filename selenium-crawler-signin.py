# Use Selenium to log into LeetCode and fetch my solved problem count.
# Note: The login page is protected by Cloudflare, so this is for practice only
# and will not work in production.

# Import Selenium-related modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set the path to the ChromeDriver executable
options=Options()
options.add_experimental_option("detach", True) # Keep the Chrome browser open after the script finishes
options.chrome_executable_path="chromedriver.exe"

# Create a driver object to control the browser via code
driver=webdriver.Chrome(options=options)

# Connect to the Leetcode Login page
driver.get("https://leetcode.com/accounts/login/")

# Enter UID and password, then sign in
usernameInput = driver.find_element(By.ID,"id_login")
passwordInput = driver.find_element(By.ID,"id_password")
usernameInput.send_keys("uid") #Enter your own uid
passwordInput.send_keys("password") #Enter your own password
signinBtn = driver.find_element(By.ID,"signin_btn")
signinBtn.send_keys(Keys.ENTER)

time.sleep(5) # Wait for 5 seconds to allow the page to load

# Below is for practice only and may not work reliably.
driver.get("https://leetcode.com/problemset/")
statElement=driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")
print(statElement.text)

driver.close()