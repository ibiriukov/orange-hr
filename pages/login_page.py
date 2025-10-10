
from utils.settings import BASE_URL
from pages.dashboard_page import DashboardPage

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.login_button = 'button[type="submit"]'

    def login(self, username, password):
        self.page.goto(BASE_URL)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        return DashboardPage(self.page)
