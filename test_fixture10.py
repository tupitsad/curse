import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestPassword:
    def test_auth(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        time.sleep(20)
        browser.find_element(By.LINK_TEXT, "Войти").click()
        input1=browser.find_element(By.ID, "id_login_email")
        input1.send_keys("tupitsadanila@yandex.ru")
        input2=browser.find_element(By.ID, "id_login_password")
        input2.send_keys("Nikogda777!")
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
        time.sleep(20)
        input4 = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea")))
        input4.send_keys(math.log(int(time.time())))
        
        button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".attempt-wrapper-buttons__button")))
        button.click()
        
        input5 = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        input6 = input5.text
        assert input6 == "Correct!", input6


        

        
