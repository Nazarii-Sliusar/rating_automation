from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LeaveFeedbackPage(BasePage):
    __input_phone = (By.ID, 'phone')
    __input_rating = (By.ID, 'rating')
    __input_name = (By.ID, 'name')
    __input_feedback = (By.ID, 'feedback')
    __input_submit = (By.ID, 'submit')

    def enter_phone(self, phone):
        self._driver.find_element(*self.__input_phone).clear()
        self._driver.find_element(*self.__input_phone).send_keys(phone)

    def enter_rating(self, rating):
        self._driver.find_element(*self.__input_rating).send_keys(rating)

    def enter_name(self, name):
        self._driver.find_element(*self.__input_name).send_keys(name)

    def enter_feedback(self, feedback):
        self._driver.find_element(*self.__input_feedback).send_keys(feedback)

    def submit_form(self):
        self._driver.find_element(*self.__input_submit).click()
