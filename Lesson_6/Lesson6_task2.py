from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст в поле
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажимаем на кнопку
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# Получаем обновленный текст кнопки
print(button.text)

driver.quit()