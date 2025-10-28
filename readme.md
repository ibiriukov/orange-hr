# OrangeHR Test Automation Framework

> ⚡ **Quick Summary for Recruiters**  
Modular test automation suite for the OrangeHR demo app using Python, Pytest, and Playwright. Demonstrates clean architecture, shared state management, and CI/CD readiness for real-world QA engineering.

<details>
  <summary>📄 Full Technical Overview</summary>

## Tech Stack

- Pytest for test orchestration and fixtures  
- Playwright for browser automation  
- Page Object Model (POM) for maintainability  
- Shared state management for cross-test data flow  
- Environment variable handling via `.env` and `config.py`  

## Test Coverage

- **Login validation** — verifies successful login and dashboard load  
- **Navigation flow** — confirms access to PIM module  
- **Employee creation** — adds a new employee and verifies details across UI sections  
- **Employee deletion** — deletes employee records and validates cleanup  
- **Dynamic data generation** — uses custom name generator for test isolation  
- **Conditional skipping** — intelligently skips tests when no data is found  

## CI/CD Integration

- Jenkins jobs triggered by GitHub commits  
- Parameterized test runs with environment control  
- Build history and job status visible in Jenkins dashboard (`Jenkins.jpg`)  

## Reporting

- Pytest generates HTML reports for each test run  
- Screenshot capture not yet implemented  
- Sample report included (`report.html`)  

## 📁 Project Structure

- `pages/` — Page Object Models  
  - `add_employee_page.py`  
  - `dashboard_page.py`  
  - `employee_list_page.py`  
  - `leave_page.py`  
  - `login_page.py`  
  - `main_page.py`  
  - `personal_details_page.py`  
  - `pim_page.py`  
  - `recruitment_page.py`  
- `tests/` — Pytest test cases  
  - `conftest.py`  
  - `test_add_delete_employee.py`  
- `utils/` — Helpers and config  
  - `common_methods.py`  
  - `data_generators.py`  
  - `settings.py`  
  - `shared_state.py`  
- `data/` — Static assets (e.g. `image.jpg`)  
- `.env` — Environment variables  
- `.gitignore` — Git exclusions  
- `config.py` — Runtime config loader  
- `pytest.ini` — Pytest config  
- `requirements.txt` — Python dependencies  
- `temp_shared_state.json` — Runtime state cache  
- `Jenkins.jpg` — Screenshot of CI integration  
- `report.html` — Sample test report  
- `README.md` — Project overview  

## Author

**Ievgen** — QA-focused engineer with deep experience in Playwright, Pytest, and CI/CD pipelines. Passionate about clean architecture, dynamic data handling, and scalable test automation.

</details>