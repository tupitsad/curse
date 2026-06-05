from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    option0 = browser.find_element(By.CSS_SELECTOR, "[id = 'treasure']")
    x = option0.get_attribute("valuex")
    y = calc(x)
    option4 = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    option4.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id = 'robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, "[type ='submit']")
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()