from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ReadFeedbackPage(BasePage):
    __input_phone = (By.ID, 'phone')
    __button_submit = (By.XPATH, '//button[@type="submit"]')
    __rating_locator = (By.XPATH, '//b')
    __feedback_text_locator = (By.XPATH, '//span[@class="feedback-text"]')
    __stars_locator = (By.XPATH, '//span[@class="star"]')
    __feedback_date_locator = (By.XPATH, '//span[@class="feedback-date"]')


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def search_feedback(self, phone):
        self._driver.find_element(*self.__input_phone).clear()
        self._driver.find_element(*self.__input_phone).send_keys(phone)
        self._driver.find_element(*self.__button_submit).click()

    def get_rating(self) -> str:
        return self._driver.find_element(*self.__rating_locator).text

    def get_feedback(self) -> str:
        return self._driver.find_element(*self.__feedback_text_locator).text

    def count_stars(self) -> int:
        return len(self._driver.find_elements(*self.__stars_locator))

    def get_feedback_date(self):
        return self._driver.find_element(*self.__feedback_date_locator).text
