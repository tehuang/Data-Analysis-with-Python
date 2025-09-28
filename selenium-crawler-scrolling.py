# Import Selenium-related modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set the path to the ChromeDriver executable
options = Options()
options.chrome_executable_path="chromedriver.exe"

# Create a driver object to control the browser via code
driver=webdriver.Chrome(options=options)

# Connect to the LinkedIn job posting page
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() # Send ESC key to the browser to close popups or modals

# Scroll the window and wait for the browser to load more content
n=0
while n<3: 
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") # Scroll the window to the bottom of the page
    time.sleep(3) # Wait for 3 seconds to allow the page to load
    n+=1

# Retrieve job titles from the webpage
titleTags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()