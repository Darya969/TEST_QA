from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

power_is_in_people = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]//p[contains(@class, "tensor_ru-Index__card-title") and contains(text(), "Сила в людях")]')
detailed = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]//a[contains(@class, "tensor_ru-link") and contains(text(), "Подробнее")]')
working = (By.XPATH, '//div[contains(@class, "tensor_ru-About__block3")]//h2[contains(@class, "tensor_ru-header-h2") and contains(text(), "Работаем")]')
container_locator = (By.CLASS_NAME, 's-Grid-container')
image_locator = (By.XPATH, './/div[contains(@class, "tensor_ru-About__block3--col-sm12")]//img')

class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def switch_to_new_tab(self, original_window):
        WebDriverWait(self.browser, 10).until(lambda d: len(d.window_handles) > 1)
        all_windows = self.browser.window_handles
        for window in all_windows:
            if window != original_window:
                self.browser.switch_to.window(window)
                break

    def is_tensor_url_opened(self):
        WebDriverWait(self.browser, 10).until(EC.url_contains("https://tensor.ru/"))
        return "https://tensor.ru/" in self.browser.current_url

    @property
    def block_is_displayed(self):
        return self.find(power_is_in_people).is_displayed()

    def detailed_click(self):
        self.find(detailed).click()

    @property
    def url_about(self):
        return "https://tensor.ru/about" in self.browser.current_url

    @property
    def working_is_displayed(self):
        return self.find(working).is_displayed()

    def wait_for_container(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(container_locator)
        )

    @property
    def get_images(self):
        container = self.find(container_locator)
        return container.find_elements(*image_locator)