from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

path = 'D:\work\selenium\chromedriver.exe'
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome(path)
    driver.get(link)

    WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    driver.find_element(By.ID, 'book').click()

    x = driver.find_element(By.ID, 'input_value').text
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    driver.quit()