import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class EmployeeListPage(BasePage):

    PAGE_URL = Links.EMPLOYEE_LIST_PAGE
    
    EMPLOYEE_NAME_INPUT = ("xpath", "//div[contains(@class, 'oxd-grid-item')]//div[contains(@class, 'oxd-input-group')]//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    
    SEARCH_BUTTON = ("xpath", "//button[@type='submit']")

    TABLE_CARD_ITEMS = ("xpath", "//div[contains(@class, 'oxd-table-card')]")

    NO_RECORDS_SPAN = ("xpath", "//span[contains(@class, 'oxd-text--span') and text() = 'No Records Found']")


    @allure.step("Enter employee name in the search field")
    def enter_employee_name_in_search_field(self, employee_name):
        employee_name_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_INPUT))
        employee_name_field.send_keys(employee_name)

    
    @allure.step(" Click on the 'Search' button ")
    def search_button_click(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step(" Check if there are no records ")
    def no_records_check(self, should_be_present=True):
        try:
            no_records_span = self.wait.until(EC.presence_of_element_located(self.NO_RECORDS_SPAN))
            is_present = no_records_span.text == "No Records Found"
            if should_be_present:
                assert is_present, f"Expected 'No Records Found' message to be present, but it was not found"
            else:
                assert not is_present, f"Expected 'No Records Found' message to be absent, but it was found"
            return is_present
        except:
            if should_be_present:
                assert False, "Expected 'No Records Found' message to be present, but element was not found"
            return False
           


        
    @allure.step("Records check")
    def records_count_check(self, expected_count):
        self.wait.until(EC.presence_of_all_elements_located(self.TABLE_CARD_ITEMS)) 
        card_items = self.driver.find_elements(*self.TABLE_CARD_ITEMS)
        actual_count = len(card_items)
        assert actual_count == expected_count, f"Expected {expected_count} items, but found {actual_count}"


      






       
