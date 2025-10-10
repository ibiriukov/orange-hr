import time

from playwright.sync_api import Page, Locator, expect

from pages.main_page import MainPage
from utils.common_methods import get_text_of_element


class PimPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page: Page = page
        self.header_breadcrumb: Locator = page.locator("span.oxd-topbar-header-breadcrumb")
        self.tabs_of_piv_navbar = page.locator(".oxd-topbar-body nav li")
        self.tabs_of_config_dropdown_in_piv_navbar = page.locator(".oxd-dropdown-menu li")

    def get_text_of_breadcrumb(self):
        return get_text_of_element(self.header_breadcrumb)

    def is_loaded(self) -> bool:
        # Wait until breadcrumb is visible and return True if it appears
        expect(self.header_breadcrumb).to_be_visible(timeout=5000)
        return True

    def select_tab_in_pim_navbar(self, tabName):
        for i in range(self.tabs_of_piv_navbar.count()):
            tab = self.tabs_of_piv_navbar.nth(i)
            text = tab.text_content().strip()
            if text == tabName:
                tab.click()

                return self._get_page_object(tabName)
        raise ValueError(f"Tab '{tabName}' not found in PIV navbar")

    def _get_page_object(self, name: str):
        name = name.strip().lower()
        if name == "add employee":
            from pages.add_employee_page import AddEmployeePage
            return AddEmployeePage(self.page)
        elif name == "employee list":
            from pages.employee_list_page import EmployeeListPage
            return EmployeeListPage(self.page)

        return None
