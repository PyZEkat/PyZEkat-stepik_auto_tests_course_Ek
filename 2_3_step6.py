from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

path = 'C:\work\selenium\chromedriver.exe'
link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome(path)
    driver.get(link)
    #time.sleep(3)

    driver.find_element(By.TAG_NAME, 'button').click()

    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(10)
    driver.quit()