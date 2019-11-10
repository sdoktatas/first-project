from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


temperature_Celsius = input('Add meg a hőméersékletet Celsiusban! ')

driver = webdriver.Chrome()

driver.get("https://www.convertworld.com/hu/homerseklet/fahrenheit.html")


input_field = driver.find_element_by_name('amount')
input_field.send_keys(temperature_Celsius)
selectFrom = Select(driver.find_element_by_id('from_temperature'))
selectFrom.select_by_visible_text('Celsius (C)')
selectTo = Select(driver.find_element_by_id('to_temperature'))
selectTo.select_by_visible_text('Fahrenheit (F)')

button = driver.find_element_by_xpath("//img[@title='Átalakít']")
button.click()

result = driver.find_element_by_id("result-to")
print(temperature_Celsius + "C = " + result.text + " Fahrenheit")

