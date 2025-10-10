# tests/conftest.py
import os
import sys
import pytest
from playwright.sync_api import sync_playwright

# (optional) dotenv load wrapped in try/except if you want
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from config import CONFIG
from pages.login_page import LoginPage

def _select_engine(p, name: str):
    name = (name or "chromium").lower()
    if name == "chromium":
        return p.chromium
    if name == "firefox":
        return p.firefox
    if name == "webkit":
        return p.webkit
    raise ValueError(f"Unsupported BROWSER='{name}'. Use chromium|firefox|webkit")

@pytest.fixture(scope="session")
def browser():
    headed = os.getenv("HEADED", "false").lower() == "true"
    browser_name = os.getenv("BROWSER", "chromium")
    with sync_playwright() as p:
        engine = _select_engine(p, browser_name)
        br = engine.launch(headless=not headed)
        yield br
        br.close()

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
