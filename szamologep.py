from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/first-project")
driver.find_element(By.ID, "a-input").send_keys("11")
driver.find_element(By.ID, "b-input").send_keys("22")


header_text = driver.find_element(By.XPATH, "//h1").text
print(header_text)
assert  header_text == "Számológép"
#driver.find_element(By.XPATH, "//input[3]").click()


driver.find_element(By.ID, "submit-button").click()

eredmeny = driver.find_element(By.ID, "result-input").get_attribute("value")
print("eredmény: " + eredmeny)
assert  eredmeny == "33"