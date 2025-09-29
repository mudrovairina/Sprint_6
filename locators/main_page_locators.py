from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы блока FAQ"""
    # Вопросы
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_2 = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_3 = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_4 = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_5 = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_6 = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_7 = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_8 = (By.ID, "accordion__heading-7")

    # Ответы
    FAQ_ANSWER_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    FAQ_ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    FAQ_ANSWER_3 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    FAQ_ANSWER_4 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    FAQ_ANSWER_5 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    FAQ_ANSWER_6 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    FAQ_ANSWER_7 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    FAQ_ANSWER_8 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")

    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (
        By.XPATH,
        './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
    )
    # Нижняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'
    )
