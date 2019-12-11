from selenium import webdriver
from selenium.webdriver.common.by import By
import math



def assert_title_is(title):
    #titleF = driver.find_element_by_xpath('//title').text
    title_feluletrol = driver.title
    assert title == title_feluletrol

def assert_header_is(header):
    header_feluletrol = driver.find_element_by_xpath("//h2").text
    assert  header == header_feluletrol

def assert_image_is_present(image):
    result = driver.find_elements_by_xpath("//img[contains(@src,'image')]".replace("image", image))
    assert len(result) > 0


def test_home_page():
    assert_title_is("PetClinic :: a Spring Framework demonstration")
    assert_header_is("Welcome")
    assert_image_is_present("pets.png")

def goto_home_page():
    go_to_home_page_button = driver.find_element_by_xpath("//li/a[@title='home page']")
    go_to_home_page_button.click()

def goto_find_owners():
    go_to_owners_button = driver.find_element_by_xpath("//li/a[@title='find owners']")
    go_to_owners_button.click()

def goto_veterinarians():
    go_to_owners_button = driver.find_element_by_xpath("//li/a[@title='veterinarians']")
    go_to_owners_button.click()

def test_find_owners_page():
    assert_title_is("PetClinic :: a Spring Framework demonstration")
    van_last_name = driver.find_element_by_xpath("//div/")



chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)


driver.get("http://localhost:8080")
#test_home_page()
#goto_home_page()
goto_find_owners()
#goto_veterinarians()


