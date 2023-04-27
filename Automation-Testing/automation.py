from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(r'./chromedriver.exe')
ops = webdriver.ChromeOptions()
chrome_browser = webdriver.Chrome(service=ser, options=ops)
chrome_browser.get('https://www.google.com/')
chrome_browser.maximize_window()
print('maximised successfully')
