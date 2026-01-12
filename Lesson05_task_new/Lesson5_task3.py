from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")

    # Очищаем поле
    input_field.clear()

    # Вводим текст "Pro"
    input_field.send_keys("Pro")

finally:
    # Закрываем браузер
    driver.quit()