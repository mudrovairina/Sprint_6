import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL


@allure.suite("FAQ на главной странице")
@allure.sub_suite("Проверка ответов на вопросы")
class TestMainPageFAQ:

    # Словарь с ожидаемыми текстами ответа
    EXPECTED_ANSWER_TEXT = {
        "PRICE": (
            "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        ),
        "MULTI_ORDER": (
            "Пока что у нас так: один заказ — один самокат. "
            "Если хотите покататься с друзьями, можете "
            "просто сделать несколько заказов — один за другим."
        ),
        "RENTAL_TIME": (
            "Допустим, вы оформляете заказ на 8 мая. "
            "Мы привозим самокат 8 мая в течение дня. "
            "Отсчёт времени аренды начинается с момента, "
            "когда вы оплатите заказ курьеру. "
            "Если мы привезли самокат 8 мая в 20:30, "
            "суточная аренда закончится 9 мая в 20:30."
        ),
        "NEXT_DAY": (
            "Только начиная с завтрашнего дня. "
            "Но скоро станем расторопнее."
        ),
        "URGENT_SUPPORT": (
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в "
            "поддержку по красивому номеру 1010."
        ),
        "BATTERY": (
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
            "суток — даже если будете кататься без передышек и во сне. "
            "Зарядка не понадобится."
        ),
        "RETURN_POLICY": (
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной "
            "записки тоже не попросим. Все же свои."
        ),
        "DELIVERY": (
            "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )
    }

    # Данные для параметризации FAQ
    FAQ_DATA = [
        (
            MainPageLocators.FAQ_QUESTION_1,
            MainPageLocators.FAQ_ANSWER_1,
            "PRICE"
        ),
        (
            MainPageLocators.FAQ_QUESTION_2,
            MainPageLocators.FAQ_ANSWER_2,
            "MULTI_ORDER"
        ),
        (
            MainPageLocators.FAQ_QUESTION_3,
            MainPageLocators.FAQ_ANSWER_3,
            "RENTAL_TIME"
        ),
        (
            MainPageLocators.FAQ_QUESTION_4,
            MainPageLocators.FAQ_ANSWER_4,
            "NEXT_DAY"
        ),
        (
            MainPageLocators.FAQ_QUESTION_5,
            MainPageLocators.FAQ_ANSWER_5,
            "URGENT_SUPPORT"
        ),
        (
            MainPageLocators.FAQ_QUESTION_6,
            MainPageLocators.FAQ_ANSWER_6,
            "BATTERY"
        ),
        (
            MainPageLocators.FAQ_QUESTION_7,
            MainPageLocators.FAQ_ANSWER_7,
            "RETURN_POLICY"
        ),
        (
            MainPageLocators.FAQ_QUESTION_8,
            MainPageLocators.FAQ_ANSWER_8,
            "DELIVERY"
        ),
    ]

    @pytest.mark.parametrize(
        "question, answer, expected_answer_key",
        FAQ_DATA
    )
    @allure.title("Проверка ответа на вопрос FAQ")
    @allure.description(
        "Открываем вопрос из FAQ и проверяем корректность ответа"
    )
    def test_faq(self, driver, question, answer, expected_answer_key):
        main_page = MainPage(driver)

        with allure.step(f"Открываем главную страницу {MAIN_PAGE_URL}"):
            main_page.open(MAIN_PAGE_URL)

        with allure.step("Открываем вопрос и получаем ответ"):
            actual_text = main_page.open_question_and_get_answer(
                question, answer
            )

        with allure.step("Сравниваем полученный ответ с ожидаемым"):
            expected_text = self.EXPECTED_ANSWER_TEXT[expected_answer_key]
            assert actual_text == expected_text, (
                f"[FAQ] Для вопроса '{question}' ожидали ответ: "
                f"'{expected_text}', но получили: '{actual_text}'"
            )
