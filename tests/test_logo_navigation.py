import allure

from pages.order_page import OrderPage
from urls import ORDER_PAGE_URL, MAIN_PAGE_URL, YANDEX_DZEN_DOMEN


@allure.suite("Редиректы логотипов")
@allure.sub_suite("Главная страница и Яндекс Дзен")
class TestLogoRedirect:

    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.description(
        "Проверяем, что при клике на логотип Самоката "
        "происходит переход на главную страницу"
    )
    def test_scooter_redirect_to_main(self, driver):
        order_page = OrderPage(driver)

        with allure.step("Открываем страницу заказа"):
            order_page.open(ORDER_PAGE_URL)

        with allure.step("Кликаем на логотип Самоката"):
            order_page.click_scooter_logo()

        with allure.step("Проверяем, что перешли на главную страницу"):
            assert driver.current_url == MAIN_PAGE_URL, (
                "Не перешли на главную страницу Самоката"
            )

    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description(
        "Проверяем, что при клике на логотип Яндекса открывается Дзен"
    )
    def test_yandex_logo_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)

        with allure.step("Открываем страницу заказа"):
            order_page.open(ORDER_PAGE_URL)

        with allure.step("Кликаем на логотип Яндекса"):
            order_page.click_yandex_logo()

        with allure.step("Переключаемся на новое окно"):
            order_page.switch_to_new_window()

        with allure.step("Проверяем URL новой страницы"):
            actual_url = driver.current_url
            assert YANDEX_DZEN_DOMEN in actual_url, (
                f"Ожидали URL, содержащий '{YANDEX_DZEN_DOMEN}', "
                f"но открылась страница с URL: '{actual_url}'"
            )
