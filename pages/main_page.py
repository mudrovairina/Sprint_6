from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная страница сайта"""

    # FAQ
    def open_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_to(question_locator)
        self.click(question_locator)
        return self.find(answer_locator).text

    # Заказ самоката
    def click_order_top(self):
        self.click(BasePageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_to(BasePageLocators.ORDER_BUTTON_BOTTOM)
        self.click(BasePageLocators.ORDER_BUTTON_BOTTOM)
