import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    __url_register = 'https://www.rating.in.ua/register'
    __input_name = (By.ID, 'name')
    __input_surname = (By.ID, 'surname')
    __input_password = (By.ID, 'password')
    __input_confirmation_password = (By.ID, 'confirmation')
    __input_phone = (By.ID, 'phone')
    __button_submit = (By.ID, 'submit')
    __checkbox_agree = (By.ID, 'checkbox')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def expected_register_url(self) -> str:
        return self.__url_register

    def enter_name(self, name: str):
        super()._send_keys(self.__input_name, name)

    def enter_surname(self, surname):
        super()._send_keys(self.__input_surname, surname)

    def enter_password(self, password):
        super()._send_keys(self.__input_password, password)

    def enter_confirm_password(self, confirm_password):
        super()._send_keys(self.__input_confirmation_password, confirm_password)

    def enter_phone(self, phone):
        super()._clear(self.__input_phone)
        super()._send_keys(self.__input_phone, phone)

    def submit_button_is_clickable(self) -> bool:
        return super()._is_clickable(self.__button_submit)

    def check_checkbox_agree(self):
        super()._click(self.__checkbox_agree)

    def submit(self):
        super()._click(self.__button_submit)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_register))

    def submit_no_wait(self):
        super()._click(self.__button_submit)

    def open(self):
        self._driver.get(self.__url_register)


