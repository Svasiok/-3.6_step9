import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = f"http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/"


def test_item_has_add(browser):
    browser.get(link)
    item = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form")
    assert item, 'no item'