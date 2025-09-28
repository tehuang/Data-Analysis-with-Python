# Browser automation screenshot
# 1. Download the ChromeDriver executable
# 2. Install the Selenium package
    # 3 main uses of Selenium browser automation:
    # A. Webpage screenshots
    # B. Web scraping
    # C. Web automation testing
# 3. Write the automation script

# Import Selenium-related modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
options = Options()
options.chrome_executable_path="chromedriver.exe"

# Create a driver object to control the browser via code
driver=webdriver.Chrome(options=options)
driver.maximize_window() # Maximize the browser window
driver.get("https://www.google.com")
driver.save_screenshot("screenshot-google.png") #screenshot
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screenshot-ntu.png") #screenshot
driver.close()