## generate under https://developer.riotgames.com/
api_key = input('API Key: ')
print(api_key)

## pull from selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

'''
Usage
set up chromedriver, if not already exists check if already exists using chromedriver --version
install chromedriver brew cask install chromedriver
find path which chromedriver
'''
driverpath = '/usr/local/bin/chromedriver'
chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome(driverpath, options=chrome_options)
driver.get('https://na.op.gg/summoner/userName=' + 'oxstormthunder')
print(driver.find_element_by_class_name("Navigation").get_attribute('innerHTML'))
# driver.quit()