from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sdoktatas.github.io/first-project")
#driver.find_element(By.ID, "a-input").send_keys("11")

first_number = int(input("Első szám? "))

second_number = int(input("Második szám? "))

expected = first_number + second_number

first_input_field = driver.find_element(By.ID, "a-input")
first_input_field.send_keys(first_number)
#first_input_field.screenshot("first-input.png")

#driver.find_element(By.ID, "b-input").send_keys("22")

second_input_field = driver.find_element(By.ID, "b-input")
second_input_field.send_keys(second_number)

header_text = driver.find_element(By.XPATH, "//h1").text
print(header_text)
assert  header_text == "Számológép"
#driver.find_element(By.XPATH, "//input[3]").click()


driver.find_element(By.ID, "submit-button").click()

eredmeny = driver.find_element(By.ID, "result-input").get_attribute("value")
print("eredmény: " + eredmeny)

driver.save_screenshot("result.png")
#assert  eredmeny == "33"
print(type(expected))
print(type(eredmeny))

assert int(eredmeny) == expected