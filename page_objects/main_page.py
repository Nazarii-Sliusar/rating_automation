from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class MainPage(BasePage):
    __url = 'https://www.rating.in.ua/'
    __logout_locator = (By.XPATH, '//a[@href="/logout"]')
    __link_read_feedbacks = (By.XPATH, '//a[@href="/read_feedback_form"]')
    __link_leave_feedback = (By.XPATH, '//a[@href="/leave_feedback_form"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def expected_url(self):
        return self.__url

    def logout_link_is_displayed(self) -> bool:
        return self._driver.find_element(*self.__logout_locator).is_displayed()

    def logout(self, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable(self.__logout_locator))
        self._driver.find_element(*self.__logout_locator).click()
        wait.until(expected_conditions.url_changes('https://www.rating.in.ua/logout'))
        wait.until(expected_conditions.url_changes('https://www.rating.in.ua/'))

    def click_leave_feedback_form(self):
        self._driver.find_element(*self.__link_leave_feedback).click()

    def click_read_feedback_link(self):
        self._driver.find_element(*self.__link_read_feedbacks).click()
