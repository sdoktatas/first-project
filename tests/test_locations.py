from selenium import webdriver

from db.db_operations import DbOperation
from pages.create_location_page import CreateLocationPage
from pages.list_locations_page import ListLocationsPage
from pages.location_details_page import LocationDetailsPage


class TestLocations:

    def setup_method(self):#test fixture
        #mi itt minden futasnal pucoljuk a db-t
        db_operation = DbOperation()
        db_operation.delete_locations()
        self.driver = webdriver.Chrome()
        self.list_page = ListLocationsPage(self.driver)
        self.create_page = CreateLocationPage(self.driver)
        self.location_details_page = LocationDetailsPage(self.driver)


    def teardown_method(self):
        self.driver.close()


    def test_empty_table(self):
        #list_page = ListLocationsPage(driver)
        self.list_page.go()
        self.list_page.assert_count_of_table_rows_is(0)

    def test_when_create_location_then_details_are_correct(self):
        #db_operation = DbOperation()
       # db_operation.delete_locations()

        #driver = webdriver.Chrome()
        #list_page = ListLocationsPage(driver)
        self.create_location()

        #location_details_page = LocationDetailsPage(driver)
        self.location_details_page.assert_details_are("Tapolca", "1.0, 1.0")
        self.location_details_page.assert_message_has_been_appeared("Location has been created.")

    def test_when_create_location_then_appears_in_table(self):
        self.create_location()

        self.location_details_page.click_to_back_to_list_link()
        self.list_page.assert_table_contains_location("Tapolca", "1.0, 1.0")

    def test_when_create_20_locations_then_appears_in_the_table(self):
        with open("../mock_data_locations.csv", encoding="UTF-8") as file:
            for line in file:
                print(line.strip())
                (name, lat, lon) = line.strip().split(",")
                self.create_location(name, f"{lat},{lon}")
        self.list_page.go()
        self.list_page.assert_count_of_table_rows_is(20)

    def create_location(self, name="Tapolca", coords="1,1"):
        self.list_page.go()
        self.list_page.click_to_create_location_link()
        # create_page = CreateLocationPage(driver)
        self.create_page.fill_create_location_form(name, coords)
        self.create_page.click_to_create_button()

