from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        """
        Инициализация главной страницы магазина.
        :param driver: WebDriver instance
        """
        self._driver = driver

    @allure.step("Выбор товаров в корзину")
    def selection_of_product(self) -> None:
        """
        Добавление трех товаров в корзину.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переход на страницу корзины.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()