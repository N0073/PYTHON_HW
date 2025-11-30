import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Устанавливаем задержку
    delay_input = driver.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys('45')

    # Нажимаем последовательность кнопок
    buttons = ['7', '+', '8', '=']
    for button in buttons:
        driver.find_element(By.XPATH, f'//span[text()="{button}"]').click()

    # Ожидаем результат и проверяем его
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

    result = driver.find_element(By.CLASS_NAME, 'screen').text
    assert result == '15', f'Ожидался результат 15, но получили {result}'
