from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"
browser.get(link)

knopka = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

option0 = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
z = option0.text
x = int(z)
y = calc(x)
option4 = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
option4.send_keys(y)


button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

print(browser.switch_to.alert.text)

time.sleep(15)