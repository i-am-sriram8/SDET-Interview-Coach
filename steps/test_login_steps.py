"""
    Rule of thumb
    Write each step so it still makes sense if the UI is completely redesigned. 
    “Click btn-submit” fails that test. “Submit the inquiry” passes.

    A good Gherkin scenario is declarative: it states the business behavior, like ‘the physician 
    submits an inquiry’, not UI mechanics like clicking a button by ID. 
    That keeps scenarios readable for non-engineers and stable when the UI changes, because the 
    click-level detail lives in step definitions and page objects.
"""


from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect

scenarios("../features/login.feature")                                      #   scenarios(...) turns every scenario in the file into a pytest test.

@given("the user is on the login page")                                     #   Steps reuse fixtures, so POM and BDD combine naturally.
def open_login(login_page):
    login_page.open()

@when(parsers.parse('the user signs in as "{role}"'))
def sign_in(login_page, role):
    email, password = get_credentials(role)
    login_page.sign_in(email, password)

@then("the dashboard is shown")
def dashboard(page):
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


"""
Pass data between steps with target_fixture

@when("the user creates an inquiry", target_fixture="inquiry_id")
def create_inquiry(...):
    return new_id
"""