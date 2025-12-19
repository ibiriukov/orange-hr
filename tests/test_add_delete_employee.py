import time

import pytest

from utils.data_generators import generate_employee_name
from utils.shared_state import save_value, load_value


def test_login(page, dashboard_page):
    assert dashboard_page.get_text_of_breadcrumb() == "Dashboard"

@pytest.mark.pim
def test_go_to_pim(page, dashboard_page):
    pim_page=dashboard_page.select_tab_in_side_panel("PIM")
    assert pim_page.is_loaded()
    assert pim_page.get_text_of_breadcrumb() == "PIM"

@pytest.mark.parametrize("run", range(2))
def test_add_employee(page, dashboard_page, run):
    emp_first_name, emp_last_name, emp_id = generate_employee_name()
    pim_page = dashboard_page.select_tab_in_side_panel("PIM")
    assert pim_page.is_loaded()
    add_employee_page = pim_page.select_tab_in_pim_navbar("Add Employee")  # 1st is tab name, 2nd dropdown item
    assert add_employee_page.get_text_of_h5_or_h6_title() == "Add Employee"
    personal_details_page = add_employee_page.add_employee(emp_first_name, emp_last_name, emp_id)
    assert personal_details_page.get_text_of_first_last_name_in_image_section() == emp_first_name + " " + emp_last_name
    assert personal_details_page.get_value_of_first_name_in_employee_content() == emp_first_name
    assert personal_details_page.get_value_of_last_name_in_employee_content() == emp_last_name

    employee_list_page = personal_details_page.select_tab_in_pim_navbar("Employee List")
    assert employee_list_page.get_text_of_h5_or_h6_title() == "Employee Information"
    employee_list_page.set_employee_name(emp_first_name + " " + emp_last_name)
    employee_list_page.click_search_btn()
    assert employee_list_page.get_number_of_table_rows() == 1
    assert employee_list_page.get_name_from_search_result("First (& Middle) Name") == emp_first_name
    assert employee_list_page.get_name_from_search_result("Last Name") == emp_last_name

@pytest.mark.delete_employee
def test_delete_employee(page, dashboard_page):
    emp_first_name, emp_last_name, emp_id = generate_employee_name()
    pim_page = dashboard_page.select_tab_in_side_panel("PIM")
    assert pim_page.is_loaded()
    add_employee_page = pim_page.select_tab_in_pim_navbar("Add Employee")  # 1st is tab name, 2nd dropdown item
    assert add_employee_page.get_text_of_h5_or_h6_title() == "Add Employee"
    personal_details_page = add_employee_page.add_employee(emp_first_name, emp_last_name, emp_id)
    assert personal_details_page.get_text_of_first_last_name_in_image_section() == emp_first_name + " " + emp_last_name
    assert personal_details_page.get_value_of_first_name_in_employee_content() == emp_first_name
    assert personal_details_page.get_value_of_last_name_in_employee_content() == emp_last_name

    employee_list_page = personal_details_page.select_tab_in_pim_navbar("Employee List")
    assert employee_list_page.get_text_of_h5_or_h6_title() == "Employee Information"
    employee_list_page.set_employee_name(emp_first_name + " " + emp_last_name)
    employee_list_page.click_search_btn()
    assert employee_list_page.get_number_of_table_rows() == 1
    assert employee_list_page.get_name_from_search_result("First (& Middle) Name") == emp_first_name
    assert employee_list_page.get_name_from_search_result("Last Name") == emp_last_name

    employee_list_page.check_single_check_box_in_table(emp_last_name, "Last Name")
    assert employee_list_page.click_delete_selected_btn()
    assert not employee_list_page.confirm_deletion()

    employee_list_page.set_employee_name(emp_first_name + " " + emp_last_name)
    employee_list_page.click_search_btn()
    assert employee_list_page.get_number_of_table_rows() == 0

    employee_list_page.set_employee_name(emp_first_name)
    employee_list_page.click_search_btn()
    if employee_list_page.get_number_of_table_rows() == 0:
        pytest.skip("No rows found — skipping test.")
    else:
        time.sleep(2) # Used for testing purposes only
        employee_list_page.check_single_check_box_in_table(emp_first_name, "First (& Middle) Name")
        assert employee_list_page.click_delete_selected_btn()
        time.sleep(1)  # Used for testing purposes only
        assert not employee_list_page.confirm_deletion()
        time.sleep(1)  # Used for testing purposes only
        employee_list_page.set_employee_name(emp_first_name)
        employee_list_page.click_search_btn()
        assert employee_list_page.get_number_of_table_rows() == 0

    time.sleep(2)



