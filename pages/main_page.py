import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница сайта"""

    @allure.step("Открываем вопрос FAQ и получаем ответ")
    def open_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_to(question_locator)
        self.click(question_locator)
        return self.find(answer_locator).text

    @allure.step("Кликаем по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликаем по нижней кнопке 'Заказать'")
    def click_order_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
