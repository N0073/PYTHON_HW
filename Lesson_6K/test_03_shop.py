import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(setup):
    driver = setup
    driver.get('https://www.saucedemo.com/')

    # Авторизация
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    # Добавление товаров в корзину
    driver.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]/following-sibling::div/button').click()
    driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]/following-sibling::div/button').click()
    driver.find_element(By.XPATH, '//div[text()="Sauce Labs Onesie"]/following-sibling::div/button').click()

    # Переход в корзину
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    driver.find_element(By.XPATH, '//button[text()="Checkout"]').click()

    # Заполнение формы
    driver.find_element(By.NAME, 'firstName').send_keys('Иван')
    driver.find_element(By.NAME, 'lastName').send_keys('Петров')
    driver.find_element(By.NAME, 'postalCode').send_keys('12345')
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    # Проверка итоговой стоимости
    total = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    assert total.text == 'Total: $58.29'