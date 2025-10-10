# tests/conftest.py
from dotenv import load_dotenv
load_dotenv()  # no-op on Jenkins (no .env), useful locally

import os
import sys
import pytest
from playwright.sync_api import sync_playwright

# Make project root importable if needed
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from config import CONFIG
from pages.login_page import LoginPage

# NOTE: Do NOT declare pytest_addoption(--headed). It conflicts with plugins.
# We control headed/headless only via env var HEADED=true|false.

@pytest.fixture(scope="session")
def browser():
    # HEADED=true -> headed (UI); anything else -> headless
    headed = os.getenv("HEADED", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(locale="en-US")
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def dashboard_page(page):
    page.goto(CONFIG["base_url"])
    login_page = LoginPage(page)
    dashboard_page = login_page.login(CONFIG["username"], CONFIG["password"])
    assert dashboard_page.is_loaded()
    return dashboard_page
