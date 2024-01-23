import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from page_objects.base_page import BasePage


class LeaveFeedbackPage(BasePage):
    __input_phone = (By.ID, 'phone')
    __input_rating = (By.ID, 'rating')
    __input_name = (By.ID, 'name')
    __input_feedback = (By.ID, 'feedback')
    __input_submit = (By.ID, 'submit')
    __url_leave_feedback_form = 'https://www.rating.in.ua/leave_feedback_form'
    __link_main_locator = (By.LINK_TEXT, 'Головна')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def enter_phone(self, phone):
        super()._clear(self.__input_phone)
        super()._send_keys(self.__input_phone, phone)

    def enter_rating(self, rating):
        super()._send_keys(self.__input_rating, rating)

    def enter_name(self, name):
        super()._send_keys(self.__input_name, name)

    def enter_feedback(self, feedback):
        super()._send_keys(self.__input_feedback, feedback)

    def submit_form(self):
        super()._click(self.__input_submit)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_leave_feedback_form))

    def click_to_main_link(self):
        if isinstance(self._driver, webdriver.Safari):
            time.sleep(1)
        super()._click(self.__link_main_locator)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_leave_feedback_form))
