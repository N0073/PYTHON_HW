from selenium import webdriver
from selenium.webdriver.common.by import By

# Конфиг
SITE = "https://www.saucedemo.com"
USER = "standard_user"
PASS = "secret_sauce"

# Данные заказа
ORDER = {
    "name": "Иван",
    "last": "Иванов",
    "zip": "123456"
}

# Товары (ID кнопок добавления)
ITEMS = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-onesie"
]

# Запуск
driver = webdriver.Firefox()
driver.implicitly_wait(3)

try:
    # 1. Логин
    driver.get(SITE)
    driver.find_element(By.ID, "user-name").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASS)
    driver.find_element(By.ID, "login-button").click()

    # 2. Добавляем товары
    for item in ITEMS:
        driver.find_element(By.ID, item).click()

    # 3. Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Оформляем
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(ORDER["name"])
    driver.find_element(By.ID, "last-name").send_keys(ORDER["last"])
    driver.find_element(By.ID, "postal-code").send_keys(ORDER["zip"])
    driver.find_element(By.ID, "continue").click()

    # 5. Проверяем сумму
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert "$58.29" in total, f"Ожидалось $58.29, получили {total}"

    # 6. Завершаем
    driver.find_element(By.ID, "finish").click()

    # 7. Проверяем успех
    success = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you" in success

    print(" Всё ок, покупка оформлена!")

finally:
    driver.quit()