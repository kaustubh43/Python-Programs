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
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys('I am very cool mate')  # Enter message buttons

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")

assert 'I am very cool mate' == output_message.text
print('assertion complete')

user_buttons2 = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(user_buttons2)

sleep(30)
