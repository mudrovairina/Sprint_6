import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для всех Page Object"""

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу заказа: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ищем элемент: {locator}")
    def find(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Скроллим до элемента: {locator}")
    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Заполняем поле {locator} значением: {value}")
    def fill(self, locator, value):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    @allure.step("Переключаемся на новое окно")
    def switch_to_new_window(self):
        # Ждём, пока новое окно появится
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        # Переключаемся на него
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Ждём, пока URL перестанет быть about:blank
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )

    @allure.step("Ожидаем, что URL станет: {expected_url}")
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, 5).until(
            EC.url_to_be(expected_url)
        )

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
