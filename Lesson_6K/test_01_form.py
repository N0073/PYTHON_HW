from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# В одну строку: ждем и сразу получаем src
src = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(3)"))
).get_attribute("src")
print(src)
driver.quit()