import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from page_objects.base_page import BasePage


class ReadFeedbackPage(BasePage):
    __url_read_feedback_page = 'https://www.rating.in.ua/read_feedback_form'
    __input_phone = (By.ID, 'phone')
    __button_submit = (By.XPATH, '//button[@type="submit"]')
    __rating_locator = (By.XPATH, '//b')
    __feedback_text_locator = (By.XPATH, '//span[@class="feedback-text"]')
    __stars_locator = (By.XPATH, '//span[@class="star"]')
    __feedback_date_locator = (By.XPATH, '//span[@class="feedback-date"]')
    __link_rating_in_ua_locator = (By.XPATH, '//a[@class="navbar-brand"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def search_feedback(self, phone):
        super()._clear(self.__input_phone)
        super()._send_keys(self.__input_phone, phone)
        super()._click(self.__button_submit)

    def get_rating(self) -> str:
        return super()._get_text(self.__rating_locator)

    def get_feedback(self) -> str:
        return super()._get_text(self.__feedback_text_locator)

    def count_stars(self) -> int:
        return len(self._driver.find_elements(*self.__stars_locator))

    def get_feedback_date(self):
        return super()._get_text(self.__feedback_date_locator)

    def click_rating_in_ua_link(self):
        if isinstance(self._driver, webdriver.Safari):
            time.sleep(1)
        super()._click(self.__link_rating_in_ua_locator)
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.url_changes(self.__url_read_feedback_page))
