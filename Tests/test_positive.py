import time
import pytest

from page_objects.feedback_about_me_page import FeedbackAboutMePage
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
        assert main_page.get_alert_text.strip() == 'Ви успішно залишили відгук про користувача!', ('Unexpected alert '
                                                                                                   'text')

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

    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_feedback_about_me(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        main_page.click_feedback_about_me()
        feedback_about_me_page = FeedbackAboutMePage(driver)
        assert feedback_about_me_page.current_url == feedback_about_me_page.expected_url(), 'Not expected URL:' + feedback_about_me_page.current_url
        assert feedback_about_me_page.link_rating_in_ua_is_displayed(), 'R@TING.IN.UA is not displayed'
        assert feedback_about_me_page.link_main_is_displayed(), 'Link "Головна" is not displayed'
        assert feedback_about_me_page.link_logout_is_displayed(), 'Logout link is not displayed'
        assert feedback_about_me_page.get_rating() == '4.25', 'Rating in Header is not as expected'
        assert feedback_about_me_page.get_feedback() == ('Олександр Р. про Nazarii: Вчасно та з комфортом. Чудова '
                                                         'людина та відмінний водій, рекомендую до поїздки на '
                                                         'блаблакарі')
        assert feedback_about_me_page.count_stars_of_1st_feedback() == 5, 'Amout of stars are not correct'
        assert feedback_about_me_page.get_feedback_date() == '2023-09-07 17:20:45', 'Date is not correct'
        assert feedback_about_me_page.footer_text().strip() == 'ZariuS ® 2023 Підтримка: +380631228234', ('Footer text is '
                                                                                                  'incorrect')

    @pytest.mark.debug
    @pytest.mark.positive
    @pytest.mark.parametrize('phone, password', (('+380631228234', '1234'),))
    def test_header_links(self, driver, phone, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(phone, password)
        main_page = MainPage(driver)
        main_page.click_read_feedback_link()
        read_feedback_page = ReadFeedbackPage(driver)
        read_feedback_page.click_rating_in_ua_link()
        assert main_page.current_url == main_page.expected_url(), 'Wrong current link:' + main_page.current_url
        main_page.click_leave_feedback_form()
        leave_feedback_page = LeaveFeedbackPage(driver)
        leave_feedback_page.click_to_main_link()
        assert main_page.current_url == main_page.expected_url(), 'Wrong current link:' + main_page.current_url