import allure
import pytest

from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import MAIN_PAGE_URL


@allure.suite("Заказ самоката")
@allure.sub_suite("Позитивные сценарии")
class TestOrderPage:
    # Валидные данные для заказа
    ORDER_VALID_DATA = [
        {
            "user": {
                "first_name": "Василиса",
                "last_name": "Иванова",
                "address": "ул. Марксистская, 5",
                "metro_station": "Таганская",
                "phone": "+79991234567"
            },
            "rent": {
                "date": "2025-10-01",
                "rental_period": "сутки",
                "color": "black",
                "comment": "Без звонка"
            }
        },
        {
            "user": {
                "first_name": "Иван",
                "last_name": "Иванов",
                "address": "ул. Гагарина, 25",
                "metro_station": "Курская",
                "phone": "+78881234567"
            },
            "rent": {
                "date": "2025-10-05",
                "rental_period": "двое суток",
                "color": "grey",
                "comment": "Позвонить за 10 минут"
            }
        }
    ]

    # Методы клика по кнопкам "Заказать"
    CLICK_METHODS = ["click_order_top", "click_order_bottom"]

    @pytest.mark.parametrize("click_method", CLICK_METHODS)
    @pytest.mark.parametrize("order_data", ORDER_VALID_DATA)
    @allure.title("Проверка успешного создания заказа самоката")
    @allure.description(
        "Проверяем весь позитивный флоу заказа самоката: "
        "выбор точки входа, заполнение формы 'Для кого самокат', "
        "заполнение формы 'Про аренду', подтверждение заказа, "
        "и появление окна подтверждения."
    )
    def test_order_scooter_flow(self, driver, click_method, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open(MAIN_PAGE_URL)
        getattr(main_page, click_method)()
        order_page.fill_order_form(**order_data["user"])
        order_page.click(OrderPageLocators.NEXT_BUTTON)
        order_page.fill_rent_form(**order_data["rent"])
        order_page.click(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        order_page.click(OrderPageLocators.ORDER_MODAL_YES_BUTTON)

        with allure.step("Проверяем успешное создание заказа"):
            header = order_page.find(OrderPageLocators.ORDER_MODAL_HEADER).text
            assert "Заказ оформлен" in header, (
                f"Ожидали сообщение 'Заказ оформлен', но получили '{header}'"
            )
