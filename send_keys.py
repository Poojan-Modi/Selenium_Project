from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(10)
sum1 = driver.find_element(By.ID, 'value1')
sum2 = driver.find_element(By.ID, 'value2')

sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD5)
sum2.send_keys(Keys.NUMPAD2,Keys.NUMPAD0)

sum_button = driver.find_element(By.CSS_SELECTOR,'button[onclick="return total()"]')
sum_button.click()

