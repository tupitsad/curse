from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
option0 = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
z = option0.text
x = int(z)
y = calc(x)
option4 = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
option4.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "[id = 'robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)