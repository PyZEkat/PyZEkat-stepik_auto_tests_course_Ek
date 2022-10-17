from selenium import webdriver
from selenium.webdriver.common.by import By
import time


path = 'C:\work\selenium\chromedriver.exe'
link = 'http://suninjuly.github.io/wait1.html'

try:
    driver = webdriver.Chrome(path)
    driver.get(link)
    time.sleep(10)

    driver.find_element(By.ID, 'verify').click()
    assert 'Verification was successful!' == driver.find_element(By.ID, 'verify_message').text

    print(driver.find_element(By.ID, 'verify_message').text)



finally:
    time.sleep(10)
    driver.quit()
