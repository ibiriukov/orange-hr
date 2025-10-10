from playwright.sync_api import Page, Locator, expect

from pages.main_page import MainPage
from utils.common_methods import get_text_of_element


class DashboardPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page: Page = page
        self.header_breadcrumb: Locator = page.locator("span.oxd-topbar-header-breadcrumb")

    def get_text_of_breadcrumb(self):
        return get_text_of_element(self.header_breadcrumb)

    def is_loaded(self) -> bool:
        # Wait until breadcrumb is visible and return True if it appears
        expect(self.header_breadcrumb).to_be_visible(timeout=5000)
        return True


