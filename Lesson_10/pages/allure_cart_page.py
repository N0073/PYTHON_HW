from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        :param driver: WebDriver instance
        """
        self._driver = driver

    @allure.step("Клик по кнопке 'Checkout'")
    def checkout(self) -> None:
        """
        Клик по кнопке Checkout для начала оформления заказа.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
