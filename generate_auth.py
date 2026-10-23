from pathlib import Path
from playwright.sync_api import sync_playwright

AUTH_DIR = Path(__file__).parent / "auth"
AUTH_DIR.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.get_by_label("Email address *").fill("customer@practicesoftwaretesting.com")
    page.get_by_label("Password *").fill("welcome01")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/account")
    context.storage_state(path=AUTH_DIR / "user1.json")
    browser.close()