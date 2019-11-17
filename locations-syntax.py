from selenium import webdriver
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")

xpath = "//tr[td[text() ='Dobogókő']]/td[3]"

coordinates = driver.find_element_by_xpath(xpath).text
# print(coordinates)
# print(type(coordinates))

xpath2 = "//tr[td[text() ='9277']]/td[2]"

nev = driver.find_element_by_xpath(xpath2).text

# print(nev)

xpath_bakonyb = "//tr[td[text() ='Bakonybánk']]/td[1]"
b_azonosito = driver.find_element_by_xpath(xpath_bakonyb).text
# print(int(b_azonosito))

xpath_zsambek = "//tr[td[text() ='Zsámbék']]/td[3]"

coordinates_zs = driver.find_element_by_xpath(xpath_zsambek).text
# print(type(coordinates_zs))
# print(float(coordinates_zs))

print('Kérdezd le Velence és Báta azonosítóját, majd add össze!')
velence_azon = driver.find_element_by_xpath("//tr[td[text() ='Velence']]/td[1]").text
bata_azon = driver.find_element_by_xpath("//tr[td[text() ='Báta']]/td[1]").text

print(int(velence_azon) + int(bata_azon))

print('Keresd ki a 9876 azonosítójú település nevét, majd írd ki az első három karakterét!')
telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9876']]/td[2]").text
print(telepules_neve[:3])
print('Keresd ki a 9898 azonosítójú település nevét, majd írd ki visszafele!')
telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9898']]/td[2]").text
print(telepules_neve[::-1])
print('Keresd ki a 9742 azonosítójú település nevét, majd írd ki a hosszát, hogy hány karakterből áll!')
telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='9742']]/td[2]").text
print(len(telepules_neve))

print('Keresd ki a 11115 azonosítójú település nevét, majd írd ki a csupa nagy és csupa kisbetűvel!')
telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='11115']]/td[2]").text
print(telepules_neve.lower())
print(telepules_neve.upper())
print('Keresd ki a 11116, 11117, 11118 azonosítójú település nevét, majd írd ki egymástól kötőjelekkel elválasztva!')
telepules_neve1 = driver.find_element_by_xpath("//tr[td[text() ='11116']]/td[2]").text
telepules_neve2 = driver.find_element_by_xpath("//tr[td[text() ='11117']]/td[2]").text
telepules_neve3 = driver.find_element_by_xpath("//tr[td[text() ='11118']]/td[2]").text

# print(telepules_neve1 + '-'+ telepules_neve2 + '-' + telepules_neve3)
print('-'.join([telepules_neve1, telepules_neve2, telepules_neve3]))
print('Írd ki Tolmács koordinátáit, de space-szel elválasztva, és tizedespont helyett tizedes vesszővel!')
tolmacs_koord = driver.find_element_by_xpath("//tr[td[text() ='Tolmács']]/td[3]").text
tolmacs_koord = tolmacs_koord.replace(","," ").replace(".",",")
print(tolmacs_koord)
print('Keresd ki a Tiszakerecseny és Tiszarád koordinátáit! Add értékül négy lebegőpontos változónak!')
coordinates_tiszakerecseny = driver.find_element_by_xpath("//tr[td[text() ='Tiszakerecseny']]/td[3]").text
coordinates_tiszarad = driver.find_element_by_xpath("//tr[td[text() ='Tiszarád']]/td[3]").text

coordinatak_tomb_tiszakerecseny = coordinates_tiszakerecseny.split(",")
print(coordinatak_tomb_tiszakerecseny)
coordinata1_x = float(coordinatak_tomb_tiszakerecseny[0])
coordinata1_y = float(coordinatak_tomb_tiszakerecseny[1])

coordinatak_tomb_tiszarad = coordinates_tiszarad.split(',')
print(coordinatak_tomb_tiszarad)
coordinata2_x = float(coordinatak_tomb_tiszarad[0])
coordinata2_y = float(coordinatak_tomb_tiszarad[1])
print('Az előző két településnek vond ki egymásból a szélességi és hosszúsági koordinátáit!')
lon_distance = coordinata1_x - coordinata2_x
print('Szélesség ' + str(coordinata1_x - coordinata2_x))
lan_distance =  coordinata1_y - coordinata2_y
print('Hosszúság' + str(coordinata1_y - coordinata2_y))

# print(coordinatak_2_tomb[0])
# print(coordinatak_2_tomb[1])

print('Írd ki, hogy a 11262 azonosítójú településben szerepel-e a margit szó (True vagy False!')
telepules_neve = driver.find_element_by_xpath("//tr[td[text() ='11262']]/td[2]").text
print('margit' in telepules_neve)

print('Bónusz: számold ki a két település távolságát km-ben!')
#p1 = [float(coordinatak_tomb_tiszakerecseny[0]), float(coordinatak_tomb_tiszakerecseny[1])]  # [4, 0]
#p2 = [float(coordinatak_tomb_tiszarad[0]), float(coordinatak_tomb_tiszarad[1])]  # [6, 6]
#distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
#print("tavolsag? " + str(distance))

tavolsag = math.sqrt(lan_distance ** 2 - lon_distance ** 2)
print("tavolsag " + str(tavolsag) + " km")



driver.close()
