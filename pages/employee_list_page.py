import time

from playwright.sync_api import Page, expect

from pages.pim_page import PimPage
from utils.common_methods import get_text_of_element, element_loaded, is_element_visible


class EmployeeListPage(PimPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.h5_h6_title = page.locator("//div[@class='oxd-layout-context']//h5")
        self.employee_name = page.locator("input[placeholder='Type for hints...']").nth(0)
        self.search_btn = page.locator("//button[@type='submit']")
        self.table_row = page.locator("//div[@class= 'oxd-table-card']")
        self.records_found_span= page.locator("//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//span[text()='(1) Record Found']")
        self.table_column_names = page.locator("//div[@role='columnheader']")
        self.table_cels = page.locator("//div[@class= 'oxd-table-card']//div[@role='cell']")
        self.table_check_boxes = page.locator("//div[@class='oxd-table-card']//div[@role='cell']//input")
        self.delete_selected_btn = page.locator("//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button")
        self.yes_delete_btn_in_modal = page.locator("//div[@role='document']//button[contains(.,'Yes, Delete')]")
        self.deletion_confirm_modal = page.locator("//div[@role='document']")

    def get_text_of_h5_or_h6_title(self):
        element_loaded(self.h5_h6_title)
        return get_text_of_element(self.h5_h6_title)

    def set_employee_name(self, name):
        element_loaded(self.employee_name)

        self.employee_name.fill(name)

    def click_search_btn(self):
        self.search_btn.click()

    def get_number_of_table_rows(self):
        #element_loaded(self.records_found_span)
        time.sleep(1)
        return self.table_row.count()

    def title_is_loaded(self) -> bool:
        expect(self.h5_h6_title).to_be_visible(timeout=5000)
        return True

    def get_name_from_search_result(self, col_name: str) -> str:
        element_loaded(self.table_column_names)  # Ensure headers are loaded

        count = self.table_column_names.count()
        for i in range(count):
            raw_text = self.table_column_names.nth(i).text_content().strip()
            header_text = raw_text.replace("AscendingDescending", "").strip().lower()
            #print(f"Header {i}: '{header_text}'")
            if header_text.lower() == col_name.strip().lower():
                # Get the first row and its cells
                first_row = self.table_row.nth(0)
                cell = first_row.locator("div[role='cell']").nth(i)
                return cell.text_content().strip()

        raise ValueError(f"Column '{col_name}' not found in headers")

    def check_single_check_box_in_table(self, name, col_name):
        element_loaded(self.table_cels)  # Ensure headers are loaded
        count = self.table_column_names.count()
        for i in range(count):
            raw_text = self.table_column_names.nth(i).text_content().strip()
            header_text = raw_text.replace("AscendingDescending", "").strip().lower()
            if header_text.lower() == col_name.strip().lower():
                number_of_ele = self.table_row.count()
                for n in range(number_of_ele):
                    row = self.table_row.nth(n)
                    cell = row.locator("div[role='cell']").nth(i)  # ✅ FIXED LINE
                    if cell.text_content().strip() == name.strip():
                        time.sleep(0.3)
                        self.table_check_boxes.nth(n).click(force=True)

    def click_delete_selected_btn(self):
        element_loaded(self.delete_selected_btn)
        self.delete_selected_btn.click()
        return self.element_is_visible()

    def confirm_deletion(self):
        element_loaded(self.yes_delete_btn_in_modal)
        self.yes_delete_btn_in_modal.click()
        return self.element_is_visible()

    def element_is_visible(self):
        return is_element_visible(self.deletion_confirm_modal, "Deletion confirm modal")

