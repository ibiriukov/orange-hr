from dotenv import load_dotenv
load_dotenv()   # will look for .env in the project root

import pytest
from gherkin.dialect import file
from playwright.sync_api import sync_playwright

import os, sys

from config import CONFIG
from pages.login_page import LoginPage

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        locale="en-US" )
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
