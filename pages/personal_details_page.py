from playwright.sync_api import Page, expect

from pages.employee_list_page import EmployeeListPage
from utils.common_methods import get_text_of_element, get_value_of_element, element_loaded


class PersonalDetailsPage(EmployeeListPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_last_name_image_section = page.locator(".orangehrm-edit-employee-name h6")
        self.fName_employee_content = page.get_by_placeholder("First Name")
        self.lName_employee_content = page.get_by_placeholder("Last Name")
        self.id_employee_content = page.locator("//div[@class='oxd-form-row']//label[text()='Employee Id']//..//..//input")

    def get_text_of_first_last_name_in_image_section(self):
        element_loaded(self.first_last_name_image_section)
        return get_text_of_element(self.first_last_name_image_section)

    def get_value_of_first_name_in_employee_content(self):
        element_loaded(self.fName_employee_content)
        return get_value_of_element(self.fName_employee_content)

    def get_value_of_last_name_in_employee_content(self):
        element_loaded(self.lName_employee_content)
        return get_value_of_element(self.lName_employee_content)

    def get_value_of_id_in_employee_content(self):
        element_loaded(self.id_employee_content)
        return get_value_of_element(self.id_employee_content)



