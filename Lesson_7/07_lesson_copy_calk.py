from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    # Метод для ввода задержки
    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay_value)

    # Метод для нажатия на кнопку
    def press_button(self, button_text):
        # Локатор ищет кнопку по её тексту
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    # Метод для получения текста с экрана результата
    def get_result_text(self):
        return self.driver.find_element(*self.result_screen).text