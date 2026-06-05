from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    find = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    x = find.text
    find1 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
    y= find1.text
    z= int(x)+int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    option3 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()