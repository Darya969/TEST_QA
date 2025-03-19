from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

contacts_menu = (By.XPATH, '//div[contains(@class, "sbisru-Header-ContactsMenu")]//div[text()="Контакты"]')
contacts_menu_link = (By.XPATH, '//div[contains(@class, "sbisru-Header-ContactsMenu__items")]//a[contains(@href, "/contacts")]//span')
logo_tensor = (By.XPATH, '//a[contains(@class, "sbisru-Contacts__logo-tensor")]')
contains_title = (By.XPATH, '//h1[contains(@class, "sbisru-h2") and contains(text(), "Контакты")]')
region = (By.XPATH, '//span[contains(@class, "sbis_ru-Region-Chooser__text") and contains(text(), "г. Москва")]')
contacts_list = (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__name") and contains(text(), "Saby - Москва (Пр-т Мира)")]')
region_panel_header = (By.XPATH, '//div[contains(@class, "sbis_ru-Region-Panel__container")]//h5[contains(@class, "sbis_ru-Region-Panel__header-text") and contains(text(), "Выберите свой регион")]')
region_panel = (By.XPATH, '//div[contains(@class, "sbis_ru-Region-Panel__container")]//span[contains(text(), "41 Камчатский край")]')
region_new = (By.XPATH, '//span[contains(@class, "sbis_ru-Region-Chooser__text") and contains(text(), "Камчатский край")]')
contacts_list_new = (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__name") and contains(text(), "Saby - Камчатка")]')
render = (By.XPATH, '//div[contains(@class, "controls-Render__wrapper")]')
saby_logo = (By.XPATH, '//div[contains(@class, "sbisru-Header__logo-img")]')
footer = (By.XPATH, '//div[contains(@class, "sbisru-Footer")]')
link_download = (By.XPATH, '//div[contains(@class, "sbisru-Footer")]//a[contains(@href, "/download") and contains(text(), "Скачать локальные версии")]')
tab_button_locator = (By.XPATH, '//div[contains(@class, "controls-TabButton__caption") and text()="Saby Plugin"]')
tab_button_with_class = (By.XPATH, '//div[contains(@class, "controls-TabButton") and contains(@class, "controls-Checked__checked")]')
tab_button_os_locator = (By.XPATH, '//span[contains(@class, "sbis_ru-DownloadNew-innerTabs__title") and text()="Windows"]')
tab_button_os_with_class = (By.XPATH, '//div[contains(@class, "controls-TabButton") and contains(@class, "controls-Checked__checked")]')

class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def menu(self):
        return self.find(contacts_menu)

    @property
    def menu_is_displayed(self):
        return self.menu.is_displayed()

    def menu_click(self):
        self.menu.click()

    def menu_link_click(self):
        self.find(contacts_menu_link).click()

    @property
    def logo_tensor_is_displayed(self):
        return self.find(logo_tensor).is_displayed()

    def logo_tensor_click(self):
        return self.find(logo_tensor).click()

    def contacts_page_exist(self):
        if "https://saby.ru/contacts" not in self.browser.current_url:
            self.menu_click()
            self.menu_link_click()
            return "https://saby.ru/contacts" in self.browser.current_url
        else:
            return "https://saby.ru/contacts" in self.browser.current_url

    @property
    def contains_title_is_displayed(self):
        return self.find(contains_title).is_displayed

    @property
    def region(self):
        return self.find(region)

    @property
    def region_is_displayed(self):
        return self.region.is_displayed

    @property
    def contacts_list_is_displayed(self):
        return self.find(contacts_list).is_displayed

    def region_click(self):
        self.region.click()

    @property
    def region_panel_is_displayed(self):
        return self.find(region_panel).is_displayed

    @property
    def region_panel_header_is_displayed(self):
        return self.find(region_panel_header).is_displayed

    @property
    def render_is_displayed(self):
        return self.find(render).is_displayed

    def region_panel_click(self):
        WebDriverWait(self.browser, 100).until(
            EC.element_to_be_clickable(region_panel)
        )
        self.find(region_panel).click()

    @property
    def region_new_is_displayed(self):
        return self.find(region_new).is_displayed

    @property
    def contacts_list_new_is_displayed(self):
        return self.find(contacts_list_new).is_displayed

    def home_page_exist(self):
        if "https://saby.ru" not in self.browser.current_url:
            self.find(saby_logo).click()
            return "https://saby.ru" in self.browser.current_url
        else:
            return "https://saby.ru" in self.browser.current_url

    @property
    def footer_is_displayed(self):
        return self.find(footer).is_displayed

    @property
    def link_download(self):
        return self.find(link_download)

    @property
    def link_download_is_displayed(self):
        return self.link_download.is_displayed

    def link_download_click(self):
        self.link_download.click()

    @property
    def tab_button(self):
        return self.find(tab_button_locator)

    @property
    def tab_button_is_displayed(self):
        return self.tab_button.is_displayed

    def check_and_click_tab(self):
        element_with_class = self.browser.find_elements(*tab_button_with_class)
        if not element_with_class:
            self.tab_button.click()

    @property
    def tab_button_os(self):
        return self.find(tab_button_os_locator)

    @property
    def tab_button_os_is_displayed(self):
        return self.tab_button_os.is_displayed

    def check_and_click_tab_os(self):
        element_with_class = self.browser.find_elements(*tab_button_os_with_class)
        if not element_with_class:
            self.tab_button_os.click()