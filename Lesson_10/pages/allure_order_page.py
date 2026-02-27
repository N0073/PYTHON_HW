from selenium.webdriver.common.by import By
import allure


class OrderPage:
    def __init__(self, driver):
        self._driver = driver
        """
        Заполняет информацию о покупателе на странице оформления заказа.
        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс
        :return: None
        """

    @allure.step("Ввод имени, фамилии, индекса пользователя")
    def information_of_buyer(self, first_name: str, last_name: str, code: str) -> None:
        """
        Заполнение информации о покупателе.
        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param code: Почтовый индекс
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(code)

    @allure.step("Клик по кнопке 'Continue'")
    def button_continue(self) -> None:
        """
        Клик по кнопке Continue для перехода к итоговой информации.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Получение итоговой суммы заказа")
    def get_result(self) -> str:
        """
        Получение итоговой суммы заказа.
        :return: Итоговая сумма заказа в строковом формате
        """
        return self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.replace('Total: ', '')
