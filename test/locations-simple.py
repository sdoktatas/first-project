from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com//locations/server")
driver.find_element(By.ID, "nameInput").send_keys("Selenium")

# driver.quit()