from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 25)

def click(locator):
    wait.until(EC.element_to_be_clickable(locator)).click()

def fill(locator, text):
    elem = wait.until(EC.presence_of_element_located(locator))
    elem.clear()
    elem.send_keys(text)

driver.get("https://www.saucedemo.com")

# Логин
fill((By.ID, "user-name"), "standard_user")
fill((By.ID, "password"), "secret_sauce")
click((By.ID, "login-button"))

# Добавить товары
click((By.ID, "add-to-cart-sauce-labs-backpack"))
click((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
click((By.ID, "add-to-cart-sauce-labs-onesie"))

# Перейти в корзину
click((By.CLASS_NAME, "shopping_cart_link"))

# Оформить заказ
click((By.ID, "checkout"))

# Заполнить форму
fill((By.ID, "first-name"), "Иван")
fill((By.ID, "last-name"), "Иванов")
fill((By.ID, "postal-code"), "123456")
click((By.ID, "continue"))

# Проверить сумму
total = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "summary_total_label"))).text
assert "$58.29" in total

# Завершить
click((By.ID, "finish"))

# Проверить успех
assert "Thank you" in driver.find_element(
    By.CLASS_NAME, "complete-header").text

print(" Тест пройден успешно!")
driver.quit()