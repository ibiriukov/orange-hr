# OrangeHR Test Automation Framework

> **Overview**  
A modular test automation suite built for the OrangeHR demo app using Python, Pytest, and Playwright. Highlights include clean architecture, shared state management, and CI/CD integration—ideal for showcasing real-world QA engineering skills.
> 
> **Highlights**
- Modular Page Object Model and shared fixtures
- Smoke/regression suites with PyTest marks and parametrization
- Parallel runs, environment config, and HTML reports
- CI-ready design (Jenkins or GitHub Actions)

<details>
  <summary>📄 Full Technical Overview</summary>

## Tech Stack

- **Pytest** — test orchestration and fixture management  
- **Playwright** — fast, reliable browser automation  
- **Page Object Model (POM)** — improves test maintainability  
- **Shared state management** — enables data flow across tests  
- **Environment config** — handled via `.env` and `config.py`  

## Test Coverage

- **Login validation** — confirms successful login and dashboard visibility  
- **Navigation flow** — verifies access to the PIM module  
- **Employee creation** — adds a new employee and checks data across UI sections  
- **Employee deletion** — removes employee records and ensures proper cleanup  
- **Dynamic data generation** — uses a custom name generator for test isolation  
- **Conditional skipping** — smartly skips tests when no relevant data is available  

## CI/CD Integration

- Jenkins jobs triggered automatically on GitHub commits  
- Supports parameterized test runs with environment control  
- Build history and job status visible in the Jenkins dashboard (`Jenkins.jpg`)  

## Reporting

- HTML reports generated via Pytest for each test run  
- Screenshot capture planned but not yet implemented  
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
- `utils/` — Helpers and configuration  
  - `common_methods.py`  
  - `data_generators.py`  
  - `settings.py`  
  - `shared_state.py`  
- `data/` — Static assets (e.g., `image.jpg`)  
- `.env` — Environment variables  
- `.gitignore` — Git exclusions  
- `config.py` — Runtime configuration loader  
- `pytest.ini` — Pytest settings  
- `requirements.txt` — Python dependencies  
- `temp_shared_state.json` — Runtime state cache  
- `Jenkins.jpg` — CI integration screenshot  
- `report.html` — Sample test report  
- `README.md` — Project overview  

## 👤 Author

**Ievgen** — QA engineer with hands-on expertise in Playwright, Pytest, and CI/CD pipelines. Focused on building scalable, maintainable test automation with clean architecture and dynamic data handling.

</details>
