from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    __alert_locator = (By.XPATH, '//div[@role="alert"]')

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def get_alert_text(self) -> str:
        return self._driver.find_element(*self.__alert_locator).text
