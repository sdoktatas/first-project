from selenium import webdriver
from selenium.webdriver.common.by import By


id = input('Add meg a státuszkódot! ')

driver = webdriver.Chrome()

driver.get("https://httpstatuses.com/")

xpath_code = "//ul/li/a[@href='/" + id + "']"
print(xpath_code)

status_code = driver.find_element(By.XPATH, xpath_code)
print(status_code.text)

driver.get("https://httpstatusdogs.com/")

xpath_dog = "//div/a[contains(@href,'" + id + "')]"
print(xpath_dog)
status_dog = driver.find_element(By.XPATH, xpath_dog)

status_dog.screenshot("dog.png")

status_dog.click()



