import time

from selenium.webdriver.common.by import By


def test_find_button(browser):
    time.sleep(15)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    text_in_button = button.get_attribute('textContent')
    assert 'Add to basket' == text_in_button
