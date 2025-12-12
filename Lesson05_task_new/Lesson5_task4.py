from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Заполняем форму
driver.find_element("id", "username").send_keys("tomsmith")
driver.find_element("id", "password").send_keys("SuperSecretPassword!")
driver.find_element("css selector", "button").click()

# Получаем текст плашки
message = driver.find_element("id", "flash").text
print(" OK MESSAGE")

driver.quit()