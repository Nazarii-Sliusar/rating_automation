from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url_domain = 'https://rating.in.ua'
    __url_login = 'https://www.rating.in.ua/login'
    __input_phone = (By.ID, 'phone')
    __input_password = (By.ID, 'password')
    __button_login = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url_domain)

    def execute_login(self, phone: str, password: str,):
        self._driver.find_element(*self.__input_phone).clear()
        self._driver.find_element(*self.__input_phone).send_keys(phone)
        self._driver.find_element(*self.__input_password).send_keys(password)
        self._driver.find_element(*self.__button_login).click()

    def expected_url_login(self) -> str:
        return self.__url_login

    def is_displayed_button_login(self, time: int = 10) -> bool:
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable(self.__button_login))
        return self._driver.find_element(*self.__button_login).is_displayed()
