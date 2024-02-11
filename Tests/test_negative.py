import time
import pytest

from page_objects.feedback_about_me_page import FeedbackAboutMePage
from page_objects.leave_feedback_page import LeaveFeedbackPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.read_feedback_page import ReadFeedbackPage
from page_objects.register_page import RegisterPage
from page_objects.enter_otp_page import EnterOtpPage


class TestNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize('phone, password', (('+380631228234', '12345'), ('+380000000000', '1111')))
    def test_user_logs_in_using_wrong_credentials(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_negative_login(phone, password)
        assert login_page.current_url == login_page.expected_url_login(), 'Wrong URL'
        assert login_page.get_alert_text.strip() == 'Невірні авторизаційні дані', 'wrong alert message'

    @pytest.mark.negative
    @pytest.mark.parametrize('name, surname, phone, password, confirm_password', (('Test', 'Test', '+380000000000', '1111', '2222'),))
    def test_registering_with_different_confirmation_password(self, driver, name, surname, phone, password, confirm_password):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.enter_name(name)
        register_page.enter_surname(surname)
        register_page.enter_password(password)
        register_page.enter_confirm_password(confirm_password)
        register_page.enter_phone(phone)
        register_page.check_checkbox_agree()
        register_page.submit_no_wait()
        assert register_page.current_url == 'https://www.rating.in.ua/register', 'wrong url link'
        assert register_page.get_alert_text.strip() == 'Паролі не збігаються', 'wrong alert message'


    @pytest.mark.negative
    @pytest.mark.parametrize('name, surname, phone, password', (('Test', 'Test', '+380631228234', '12345678'),))
    def test_existing_user_tries_register(self, driver, name, surname, phone, password):
        main_page = MainPage(driver)
        main_page.open()
        login_page = LoginPage(driver)
        login_page.click_register()
        register_page = RegisterPage(driver)
        assert register_page.current_url == register_page.expected_register_url(), 'Wrong URL'
        register_page.enter_name(name)
        register_page.enter_surname(surname)
        register_page.enter_password(password)
        register_page.enter_confirm_password(password)
        register_page.enter_phone(phone)
        register_page.check_checkbox_agree()
        register_page.submit_no_wait()
        assert register_page.current_url == register_page.expected_register_url(), 'Wrong URL'
        assert register_page.get_alert_text.strip() == ('Користувач з таким номером телефону уже зареєестрований. '
                                                        'Підтримка: +380631228234')

    @pytest.mark.negative
    @pytest.mark.parametrize('phone, password', (('+380', '1111'), ('+38000000000', '1111'), ('+3800000000000', '1111')))
    def test_error_appears_on_login_if_phone_not_13(self, driver, phone, password):
        main_page = MainPage(driver)
        main_page.open()
        login_page = LoginPage(driver)
        login_page.execute_negative_login(phone, password)
        assert login_page.current_url == login_page.expected_url_login(), 'Wrong URL'
        assert login_page.get_alert_text.strip() == ('Ви ввели невірний формат телефону. Вкажіть номер телефону у '
                                                     'форматі +380...'), 'wrong alert message'

    @pytest.mark.debug
    @pytest.mark.negative
    @pytest.mark.parametrize('name, surname, phone, password', (('Test', 'Test', '+38063122823', '12345678'),))
    def test_error_appears_on_register_if_phone_not_13(self, driver, name, surname, phone, password):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.enter_name(name)
        register_page.enter_surname(surname)
        register_page.enter_password(password)
        register_page.enter_confirm_password(password)
        register_page.enter_phone(phone)
        register_page.check_checkbox_agree()
        register_page.submit_no_wait()
        assert register_page.current_url == register_page.expected_register_url(), 'Wrong URL'
        assert register_page.get_alert_text.strip() == ('Ви ввели невірний формат телефону. Вкажіть номер телефону у '
                                                        'форматі +380...')