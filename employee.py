from selenium import webdriver

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

def delete_by_azonosito(azonosito):
    to_delete = driver.find_element_by_xpath("table/tbody/tr[td[a[text()= '5bc']]]/td[last()]/form/input[@type = 'submit']")
    to_delete.click()