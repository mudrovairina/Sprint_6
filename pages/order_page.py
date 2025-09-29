import allure
from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Cтраница заказа самоката"""

    # Локаторы для выбора периода аренды
    RENTAL_PERIODS = {
        "сутки": OrderPageLocators.RENTAL_PERIOD_DAY,
        "двое суток": OrderPageLocators.RENTAL_PERIOD_TWO_DAYS
    }

    # Локаторы цветов самоката
    COLORS = {
        "black": OrderPageLocators.SCOOTER_COLOR_BLACK,
        "grey": OrderPageLocators.SCOOTER_COLOR_GREY
    }

    @allure.step("Заполняем форму 'Для кого самокат'")
    def fill_order_form(
            self,
            first_name,
            last_name,
            address,
            metro_station,
            phone
    ):
        self.fill(OrderPageLocators.NAME_INPUT, first_name)
        self.fill(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.fill(OrderPageLocators.ADDRESS_INPUT, address)
        self.fill(OrderPageLocators.PHONE_INPUT, phone)
        self._choose_metro_station(metro_station)

    @allure.step("Заполняем форму 'Про аренду'")
    def fill_rent_form(self, date, rental_period, comment=None, color=None):
        self.fill(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.DROPDOWN_ARROW)
        self.click(self.RENTAL_PERIODS[rental_period])

        if color:
            self._choose_color(color)

        if comment:
            self.fill(OrderPageLocators.COMMENT_INPUT, comment)

    # Вспомогательные методы
    def _choose_metro_station(self, station_name):
        """Выбирает станцию метро из выпадающего списка"""
        metro_input = self.find(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(station_name)
        self.click((By.XPATH, f".//div[text()='{station_name}']"))

    def _choose_color(self, color):
        """Выбирает цвет самоката"""
        color = color.lower()
        self.click(self.COLORS[color])

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo(self):
        """Кликает на логотип Самоката"""
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликает на логотип Яндекса"""
        self.click(OrderPageLocators.YANDEX_LOGO)
