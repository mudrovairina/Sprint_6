from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для всех Page Object"""

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def find(self, locator):
        """Найти и вернуть видимый элемен"""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Кликнуть по элементу после ожидания кликабельности"""
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def scroll_to(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def fill(self, locator, value):
        """Очистить поле и ввести текст"""
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    def switch_to_new_window(self):
        """Переключиться на только что открытое окно"""
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
