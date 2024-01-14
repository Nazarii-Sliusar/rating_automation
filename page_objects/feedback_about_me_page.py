from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class FeedbackAboutMePage(BasePage):
    __url_feedback_about_me = 'https://www.rating.in.ua/feedback_about_me'
    __link_rating_in_ua_locator = (By.XPATH, '//a[@class="navbar-brand"]')
    __link_main_locator = (By.LINK_TEXT, 'Головна')
    __link_logout_locator = (By.XPATH, '//a[@href="/logout"]')
    __rating_locator = (By.XPATH, '//b')
    __feedback_text_locator = (By.XPATH, '//span[@class="feedback-text"]')
    __feedback_1st_locator = (By.XPATH, '(//div[@class="feedback-item"])[1]/span[@class="star"]')
    __feedback_date_locator = (By.XPATH, '//span[@class="feedback-date"]')
    __text_footer = (By.XPATH, '//footer')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def expected_url(self):
        return self.__url_feedback_about_me

    def link_rating_in_ua_is_displayed(self) -> bool:
        return super()._is_displayed(self.__link_rating_in_ua_locator)

    def link_main_is_displayed(self) -> bool:
        return super()._is_displayed(self.__link_main_locator)

    def link_logout_is_displayed(self) -> bool:
        return super()._is_displayed(self.__link_logout_locator)

    def get_rating(self) -> str:
        return super()._get_text(self.__rating_locator)

    def get_feedback(self) -> str:
        return super()._get_text(self.__feedback_text_locator)

    def count_stars_of_1st_feedback(self) -> int:
        return len(super()._find_elements(self.__feedback_1st_locator))

    def get_feedback_date(self):
        return super()._get_text(self.__feedback_date_locator)

    def footer_text(self) -> str:
        return super()._get_text(self.__text_footer)
