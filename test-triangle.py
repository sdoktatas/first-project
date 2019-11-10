from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/first-project/triangles.html")
input_a = driver.find_element_by_id("a-input")
input_b = driver.find_element_by_id("b-input")
input_c = driver.find_element_by_id("c-input")
button = driver.find_element_by_id("calculate-button")


input_a.send_keys("3")
input_b.send_keys("3")
input_c.send_keys("3")
button.click()

