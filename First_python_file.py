from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#rom selenium.webdriver import message

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")  # Коректно

#time.sleep(0.30)
driver.implicitly_wait(5)
search = driver.find_element(By.ID, 'L2AGLb')
search.send_keys(Keys.ENTER)

#time.sleep(0.30)
driver.implicitly_wait(5)
search_line = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

search_line.send_keys('Amazon', Keys.ENTER)
driver.implicitly_wait(5)
#time.sleep(1)

actual_text = 'Amazon'
expected_text = driver.find_element(By.CSS_SELECTOR, 'div.PZPZlf.ssJ7i.B5dxMb[data-attrid="title"]').text

assert expected_text == actual_text, f'Test passed!  Actual text -> {actual_text} == expected -> {expected_text}'
#time.sleep(5)
driver.implicitly_wait(5)
driver.quit()