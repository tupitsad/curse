from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)
raz = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter first name"]')
raz.send_keys("aaaa")
dva = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter last name"]')
dva.send_keys("aaaa")
tri = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter email"]')
tri.send_keys("aaaa")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
element.send_keys(file_path)           # добавляем к этому пути имя файла 

chtr = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

time.sleep(10)