# Import Selenium-related modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
options = Options()
options.chrome_executable_path="chromedriver.exe"

# Create a driver object to control the browser via code
driver=webdriver.Chrome(options=options)

# Connect to the PTT Stock Board
driver.get("https://www.ptt.cc/bbs/stock/index.html")
#print(driver.page_source) # Get the page source

# Retrieve article titles from the Stock Board
tags = driver.find_elements(By.CLASS_NAME,"title") # Find all tags with class attribute "title"
for tag in tags:
    print(tag.text)

# Retrieve article titles from the previous page
link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click() # Simulate a user clicking a link tag
tags = driver.find_elements(By.CLASS_NAME,"title") # Find all tags with class attribute "title"
for tag in tags:
    print(tag.text)

driver.close()