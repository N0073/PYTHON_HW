from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def calculate(self, expression):
        for char in expression:
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{char}']"))
            )
            button.click()

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text