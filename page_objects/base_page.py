from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    __alert_locator = (By.XPATH, '//div[@role="alert"]')

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    @property
    def get_alert_text(self) -> str:
        return self._get_text(self.__alert_locator)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> list[WebElement]:
        self._wait_until_element_is_visible(locator)
        return self._driver.find_elements(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _is_displayed(self, locator: tuple, time: int = 10) -> bool:
        try:
            self._wait_until_element_is_visible(locator, time)
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        # тут якась хуйня. треба ще раз переввірити нащо це додавати як що вже є ексепшин,
        # але без цього  тест падає з помилкою TimeoutException
        except TimeoutException:
            return False

    def _is_clickable(self, locator: tuple) -> bool:
        try:
            wait = WebDriverWait(self._driver, 0.1)
            wait.until(expected_conditions.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def _clear(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable(locator))
        self._find(locator).clear()

    def _send_keys(self, locator: tuple, text: str):
        self._wait_until_element_is_visible(locator)
        self._find(locator).send_keys(text)

