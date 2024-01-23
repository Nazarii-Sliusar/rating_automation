from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class EnterOtpPage(BasePage):
    __url_enter_otp = 'https://www.rating.in.ua/enter_otp'
    __message_locator = (By.XPATH, '//form[@action="/enter_otp"]/p')
    __input_enter_otp = (By.ID, 'otp')
    __button_submit = (By.XPATH, '//button[@type="submit"]')
    __timer_locator = (By.ID, 'timer')
    __button_resend = (By.ID, 'resend')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def expected_url_enter_otp(self) -> str:
        return self.__url_enter_otp

    def get_message(self) -> str:
        return super()._get_text(self.__message_locator)

    def enter_otp_input_is_displayed(self) -> bool:
        return super()._is_displayed(self.__input_enter_otp)

    def confirm_button_is_displayed(self) -> bool:
        return super()._is_displayed(self.__button_submit)

    def timer_text(self) -> str:
        return super()._get_text(self.__timer_locator)

    def resend_sms_button_is_displayed(self) -> bool:
        return super()._is_displayed(self.__button_resend, 1)

    def click_resend_button(self):
        super()._click(self.__button_resend)



