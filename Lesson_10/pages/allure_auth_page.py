from selenium.webdriver.common.by import By
import allure


class AuthPage:
    def __init__(self, driver):
        """
        Инициализация страницы авторизации
        :param driver: WebDriver instance
        """
        self._driver = driver

    @allure.step("Ввод логина и пароля")
    def login(self, username: str, password: str) -> None:
        """
        Ввод логина и пароля пользователя.
        :param username: Логин пользователя
        :param password: Пароль пользователя
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    @allure.step("Клик по кнопке 'Login' для авторизации")
    def login_button(self) -> None:
        """
        Клик по кнопке Login для завершения авторизации.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()