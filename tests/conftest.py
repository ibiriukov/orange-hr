# tests/conftest.py
try:
    from dotenv import load_dotenv
    load_dotenv()   # no-op on Jenkins (no .env); useful locally
except Exception:
    pass

import os
import sys
import pytest
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from config import CONFIG
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    headed = os.getenv("HEADED", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    ctx = browser.new_context(locale="en-US")
    pg = ctx.new_page()
    yield pg
    ctx.close()

@pytest.fixture
def dashboard_page(page):
    page.goto(CONFIG["base_url"])
    login_page = LoginPage(page)
    dash = login_page.login(CONFIG["username"], CONFIG["password"])
    assert dash.is_loaded()
    return dash
