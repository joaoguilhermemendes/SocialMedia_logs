import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service() # Initialize a Chrome web driver instance
options = webdriver.ChromeOptions() # Select Chrome as the default browser
driver = webdriver.Chrome(service=service, options=options) # Start the WebDriver with 'options' and 'service' defined

url = 'https://www.instagram.com/'
driver.get(url)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("joao_guilherme26")
password.send_keys("qafecv12345")

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)
alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()


input("Press any key to close browser... ")