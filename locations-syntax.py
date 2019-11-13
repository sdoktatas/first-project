from selenium import webdriver
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")


xpath = "//tr[td[text() ='Dobogókő']]/td[3]"

coordinates = driver.find_element_by_xpath(xpath).text
#print(coordinates)
#print(type(coordinates))

xpath2 = "//tr[td[text() ='9277']]/td[2]"

nev = driver.find_element_by_xpath(xpath2).text

#print(nev)

xpath_bakonyb = "//tr[td[text() ='Bakonybánk']]/td[1]"
b_azonosito = driver.find_element_by_xpath(xpath_bakonyb).text
#print(int(b_azonosito))

xpath_zsambek = "//tr[td[text() ='Zsámbék']]/td[3]"

coordinates_zs = driver.find_element_by_xpath(xpath_zsambek).text
#print(type(coordinates_zs))
#print(float(coordinates_zs))


velence_azon = driver.find_element_by_xpath("//tr[td[text() ='Velence']]/td[1]").text
bata_azon = driver.find_element_by_xpath("//tr[td[text() ='Báta']]/td[1]").text

print(int(velence_azon) + int(bata_azon))

telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9876']]/td[2]").text
print(telepules_neve[:3])

telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9898']]/td[2]").text
print(telepules_neve[::-1])

telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9742']]/td[2]").text
print(len(telepules_neve))


telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='11115']]/td[2]").text
print(telepules_neve.lower())
print(telepules_neve.upper())

telepules_neve1 = driver.find_element_by_xpath("//tr[td[text() ='11116']]/td[2]").text
telepules_neve2 = driver.find_element_by_xpath("//tr[td[text() ='11117']]/td[2]").text
telepules_neve3 = driver.find_element_by_xpath("//tr[td[text() ='11118']]/td[2]").text

print(telepules_neve1 + '-'+ telepules_neve2)




coordinates1 = driver.find_element_by_xpath("//tr[td[text() ='Tiszakerecseny']]/td[3]").text
coordinates2 = driver.find_element_by_xpath("//tr[td[text() ='Tiszarád']]/td[3]").text

coordinatak_1_tomb = coordinates1.split(",")
print(coordinatak_1_tomb[0])
print(coordinatak_1_tomb[1])
coordinata1_x = float(coordinatak_1_tomb[0])
coordinata1_y = float(coordinatak_1_tomb[1])
coordinatak_2_tomb = coordinates2.split(',')
coordinata2_x = float(coordinatak_2_tomb[0])
coordinata2_y = float(coordinatak_2_tomb[1])

print(coordinata1_x - coordinata2_x)
print(coordinata1_y - coordinata2_y)


#print(coordinatak_2_tomb[0])
#print(coordinatak_2_tomb[1])



p1 = [float(coordinatak_1_tomb[0]),float(coordinatak_1_tomb[1])]#[4, 0]
p2 = [float(coordinatak_2_tomb[0]),float(coordinatak_2_tomb[1])]# [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print("tavolsag " + str(distance))



driver.close()
