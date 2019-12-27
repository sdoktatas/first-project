from selenium import webdriver

from db.db_operations import DbOperation
from pages.create_location_page import CreateLocationPage
from pages.list_locations_page import ListLocationsPage
from pages.location_details_page import LocationDetailsPage

db_operation = DbOperation()
db_operation.delete_locations()
driver = webdriver.Chrome()

list_page = ListLocationsPage(driver)#peldanyositunk
list_page.go()
list_page.assert_title_is_ok()
#list_page.assert_table_contains_location("hely", "10.0, 34.0")
list_page.assert_count_of_table_rows_is(0)
list_page.click_to_create_location_link()

create_page = CreateLocationPage(driver)
create_page.fill_create_location_form("Tapolca","1,1")

create_page.click_to_create_button()

#list_page.go()
loc_details_page = LocationDetailsPage(driver)
loc_details_page.click_to_back_to_list_link()

list_page.assert_count_of_table_rows_is(1)
list_page.assert_table_contains_location("Tapolca", "1.0, 1.0")