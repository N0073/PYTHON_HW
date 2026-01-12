from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка браузера Chrome
driver = webdriver.Chrome()

try:
    # Открытие страницы с динамическим ID
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ожидание и клик по кнопке с использованием класса
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()

    print("Успешный клик по кнопке с динамическим ID")
finally:
    # Закрытие браузера
    driver.quit()