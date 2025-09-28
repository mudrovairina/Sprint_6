from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа самоката"""

    # Локаторы формы "Для кого самокат"
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # Локаторы формы 'Про аренду'
    DATE_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']"
    )
    DROPDOWN_ARROW = (By.CSS_SELECTOR, "span.Dropdown-arrow")
    RENTAL_PERIOD_DAY = (By.XPATH, ".//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, ".//div[text()='двое суток']")
    SCOOTER_COLOR_BLACK = (By.XPATH, ".//label[@for='black']")
    SCOOTER_COLOR_GREY = (By.XPATH, ".//label[@for='grey']")
    COMMENT_INPUT = (
        By.XPATH,
        ".//input[@placeholder='Комментарий для курьера']"
    )

    # Локатор кнопки 'Да' в форме 'Хотите оформить заказ'
    ORDER_MODAL_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")

    # Локатор окна с сообщением об успешном создании заказа'
    ORDER_MODAL_HEADER = (
        By.XPATH,
        ".//div[contains(text(), 'Заказ оформлен')]"
    )

    # Локаторы логотипов
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
