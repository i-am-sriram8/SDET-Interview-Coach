"""
    What is the Page Object Model and why use it?
    Each page or component gets a class that holds its locators and actions.
    Tests call methods like login_page.sign_in(...) instead of touching selectors. 
    When the UI changes you fix one class instead of 50 tests 
""" 

# Page Object
import re, pytest
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Sign in")

    def open(self):
        self.page.goto("/login")

    def sign_in(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()

def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.sign_in("physician@test.com", "secret")
    expect(page).to_have_url(re.compile(r".*/dashboard"))


#   Above same thing with fixture
#   the below one should be defined in the confest.py
@pytest.fixture
def login_page(page):           #   asks for the built-in 'page' fixture
    return LoginPage(page)      #   builds the page object once here

#   test file
def test_valid_login(login_page):
    login_page.open()
    login_page.sign_in("physician@test.com", "secret")