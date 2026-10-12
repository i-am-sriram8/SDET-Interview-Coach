with context.expect_page() as new_page_info:
    page.get_by_role("link", name="View report").click()

new_page = new_page_info.value
new_page.wait_for_load_state()
expect(new_page).to_have_title("Report")