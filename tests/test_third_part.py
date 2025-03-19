from pages.sbis import SbisPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import re

def test_home_page_exist(browser):
    sbis_page = SbisPage(browser)
    sbis_page.home_page_exist()

def test_footer_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.footer_is_displayed

def test_link_download_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.link_download_is_displayed

def test_link_download_click(browser):
    sbis_page = SbisPage(browser)
    sbis_page.link_download_click()

def test_tab_button_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.tab_button_is_displayed

def test_saby_plugin_click(browser):
    sbis_page = SbisPage(browser)
    sbis_page.check_and_click_tab()

def test_windows_click(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.tab_button_os_is_displayed
    sbis_page.check_and_click_tab_os()

def test_download(browser):
    plugin_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.sbis_ru-DownloadNew-loadLink__link.js-link'))
    )
    plugin_link.click()

    link_text = plugin_link.text
    size_match = re.search(r'\(Exe\s+([\d.]+)\s+МБ\)', link_text)
    if size_match:
        expected_size_mb = float(size_match.group(1))

    plugin_url = plugin_link.get_attribute('href')
    response = requests.get(plugin_url)
    with open('sbis_plugin_installer.exe', 'wb') as file:
        file.write(response.content)

    file_path = 'sbis_plugin_installer.exe'
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    tolerance = 0.01
    assert abs(
        file_size_mb - expected_size_mb) < tolerance