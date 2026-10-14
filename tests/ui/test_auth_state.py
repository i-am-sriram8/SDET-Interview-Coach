# one-time login, saves cookies and local storage
context = browser.new_context()
page = context.new_page()
page.goto("https://www.example.in/login")
page.get_by_label("Email").fill(USER)
page.get_by_label("Password").fill(PASSWORD)
page.get_by_role("button", name="Sign in").click()
context.storage_state(path="auth/physician.json")

# later tests start already logged in
context = browser.new_context(storage_state="auth/physician.json")

"""
    With pytest-playwright, override the context args in confest.py
"""

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "storage_state": "auth/physician.json"}