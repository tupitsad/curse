import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import time

def test_language(browser, parser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR,"html.no-js body#default.default div.container-fluid.page div.page_inner div.content div#content_inner article.product_page div.row div.col-sm-6.product_main form#add_to_basket_form.add-to-basket button.btn.btn-lg.btn-primary.btn-add-to-basket")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    assert button