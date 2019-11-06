from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/first-project")
driver.find_element(By.NAME, "a").send_keys("1")
driver.find_element(By.NAME, "b").send_keys("2")


header_text = driver.find_element(By.XPATH, "//h1").text
print(header_text)
assert  header_text == "Számológép"
driver.find_element(By.XPATH, "//input[3]").click()
#driver.find_element(By.ID, "submitButton").click()

