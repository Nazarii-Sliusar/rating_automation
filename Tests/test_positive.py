import time
import pytest

from page_objects.leave_feedback_page import LeaveFeedbackPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.read_feedback_page import ReadFeedbackPage


class TestPositive:
    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_login(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        assert main_page.current_url == main_page.expected_url(), 'Wrong current link:' + main_page.current_url
        assert main_page.logout_link_is_displayed(), 'Logout link is not displayed'

    @pytest.mark.debug
    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_logout(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        main_page.logout()
        assert login_page.current_url == login_page.expected_url_login(), 'Wrong current Login link'
        assert login_page.is_displayed_button_login(), 'Login button is not displayed'

    # @pytest.mark.debug
    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_leave_feedback(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        main_page.click_leave_feedback_form()
        leave_feedback_page = LeaveFeedbackPage(driver)
        leave_feedback_page.enter_phone('+380000000000')
        leave_feedback_page.enter_rating('5')
        leave_feedback_page.enter_name('Test Testenko')
        leave_feedback_page.enter_feedback('Test Test Test 123 !@#$%;" ')
        leave_feedback_page.submit_form()
        main_page = MainPage(driver)
        assert main_page.current_url == main_page.expected_url(), 'Wrong current link:' + main_page.current_url
        assert main_page.get_alert_text == 'Ви успішно залишили відгук про користувача!', 'Unexpected alert text'

    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_read_feedbacks(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        main_page.click_read_feedback_link()
        read_feedback_page = ReadFeedbackPage(driver)
        read_feedback_page.search_feedback('+380969276973')
        assert read_feedback_page.get_rating() == '5.0', 'Rating is not as expected'
        assert read_feedback_page.get_feedback() == ('Назарій С. про Володимир: Надійна та відповідальна людина. Все '
                                                     'про що ми домовлялись завжди відповідало дійсності. Угоди були '
                                                     'дотримані, а справи - завершувались успіхом. Рекомендую до '
                                                     'співпраці!')
        assert read_feedback_page.count_stars() == 6, 'Amount of stars != 6 but should'
        assert read_feedback_page.get_feedback_date() == '2023-11-30 17:06:41', 'Feedback date is not matching'
