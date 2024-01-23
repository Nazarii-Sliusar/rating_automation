from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url_domain = 'https://rating.in.ua'
    __url_login = 'https://www.rating.in.ua/login'
    __input_phone = (By.ID, 'phone')
    __input_password = (By.ID, 'password')
    __button_login = (By.XPATH, '//button[@type="submit"]')
    __button_register = (By.XPATH, '//a[@href="/register"]')


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url_domain)

    def execute_login(self, phone: str, password: str,):
        super()._clear(self.__input_phone)
        super()._send_keys(self.__input_phone, phone)
        super()._send_keys(self.__input_password, password)
        super()._click(self.__button_login)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_login))

    def execute_negative_login(self, phone: str, password: str,):
        super()._clear(self.__input_phone)
        super()._send_keys(self.__input_phone, phone)
        super()._send_keys(self.__input_password, password)
        super()._click(self.__button_login)

    def expected_url_login(self) -> str:
        return self.__url_login

    def is_displayed_button_login(self) -> bool:
        return super()._is_displayed(self.__button_login)

    def click_register(self):
        super()._click(self.__button_register)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_login))
