from selenium import webdriver
import pytest

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(100)
    browser.get('https://sbis.ru/')
    yield browser
    browser.quit()

@pytest.fixture(scope='module')
def original_window(browser):
    original = browser.current_window_handle
    yield original
    browser.switch_to.window(original)