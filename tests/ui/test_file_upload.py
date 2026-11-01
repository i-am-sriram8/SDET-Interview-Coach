from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.example.in")
    page.get_by_label("Upload document").set_input_files("data/consent.pdf")

    with page.expect_download() as download_info:
        page.get_by_role("button", name="Export").click()
    download = download_info.value
    download.save_as("downloads/export.csv")