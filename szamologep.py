from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/first-project")
driver.find_element(By.NAME, "a").send_keys("1")
driver.find_element(By.NAME, "b").send_keys("2")



