from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
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