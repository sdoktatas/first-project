from selenium import webdriver
from selenium.webdriver.common.by import By

def print_coords_by_name(name):
    xpath = "//tr[td[text() ='name']]/td[3]".replace("name",name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

def coords_by_name(name):
    xpath = "//tr[td[text() ='name']]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    return coords


def name_by_azonosito(azonosito):
    xpath = "//tr[td[text() ='azonosito']]/td[2]".replace("azonosito", azonosito)
    name = driver.find_element(By.XPATH, xpath).text
    return  name

def hely_felvetele(nev, koordinata):
    input_name = driver.find_element_by_id("nameInput")
    input_coords = driver.find_element_by_id("coordsInput")
    button = driver.find_element_by_xpath("//button[@class = 'btn btn-primary']")
    print(button)
    input_name.send_keys(nev)
    input_coords.send_keys(koordinata)
    button.click()





driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")
print_coords_by_name("Abádszalók")
print_coords_by_name("Abasár")
print_coords_by_name("Báta")

print(coords_by_name("Abádszalók"))

print(name_by_azonosito('9277'))

hely_felvetele('KedvencHelyem','48,21')







