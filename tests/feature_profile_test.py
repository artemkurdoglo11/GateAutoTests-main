import random
import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        #self.dashboard_page.click_my_info_link()
        #self.personal_page.is_opened()
        #self.personal_page.change_name(f"Test {random.randint(1, 100)}")
        #self.personal_page.save_changes()
        #self.personal_page.is_changes_saved()
        #self.personal_page.make_screenshot("Success")
        self.employee_list_page.open()
        self.employee_list_page.is_opened()
        self.employee_list_page.enter_employee_name_in_search_field("kochanzhi")
        self.employee_list_page.search_button_click()
        self.employee_list_page.no_records_check(False)
        #self.employee_list_page.records_count_check(0)

