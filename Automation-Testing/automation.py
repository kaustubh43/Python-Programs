from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

ser = Service(executable_path='./chromedriver.exe')
ops = webdriver.ChromeOptions()
chrome_browser = webdriver.Chrome(service=ser, options=ops)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo ' in chrome_browser.title
button_text = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
print(button_text.get_attribute('innerHTML'))

sleep(20)
