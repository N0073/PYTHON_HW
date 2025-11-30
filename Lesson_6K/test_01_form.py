import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Данные для заполнения формы
    form_data = {
        'first-name': 'Иван',
        'last-name': 'Петров',
        'address': 'Ленина, 55-3',
        'e-mail': 'test@skypro.com',
        'phone': '+7985899998787',
        'city': 'Москва',
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
    }

    # Заполняем все поля кроме zip-code
    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    # Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем что поле zip-code подсвечено красным
    zip_code_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#zip-code.alert-danger'))
    )
    assert 'alert-danger' in zip_code_error.get_attribute('class')

    # Проверяем что все остальные поля подсвечены зеленым
    for field_name in form_data.keys():
        field_success = driver.find_element(By.CSS_SELECTOR, f'#{field_name}.alert-success')
        assert 'alert-success' in field_success.get_attribute('class')
