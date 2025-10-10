import time
from pathlib import Path

from playwright.sync_api import Page, expect

from pages.personal_details_page import PersonalDetailsPage
from pages.pim_page import PimPage
from utils.common_methods import get_text_of_element


class AddEmployeePage(PimPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.h5_h6_title = page.locator("//div[@class='oxd-layout-context']//h6 | //div[@class='oxd-layout-context']//h5")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.save_btn = page.get_by_role("button", name="save")
        self.employee_id = page.locator("//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input")
        self.photo_container = page.locator("div.orangehrm-employee-image, div.orangehrm-photo-container")
        self.photo_input = self.photo_container.locator("input[type='file']")

    def get_text_of_h5_or_h6_title(self):
        return get_text_of_element(self.h5_h6_title)

    def title_is_loaded(self) -> bool:
        # Wait until breadcrumb is visible and return True if it appears
        expect(self.h5_h6_title).to_be_visible(timeout=5000)
        return True

    def add_employee(self, fName, lName, emp_id):
        # ... fill first/last/id, upload photo, etc.
        self.save_btn.click()

        # Wait for navigation to Personal Details
        self.page.wait_for_url("**/pim/viewPersonalDetails/**", timeout=15000)
    
        # Wait until first name input is visible and populated (page fully rendered)
        first_name_input = self.page.locator("input[name='firstName']")
        expect(first_name_input).to_be_visible(timeout=10000)

        return PersonalDetailsPage(self.page)

