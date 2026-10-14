rows = page.locator("table tbody tr")
expect(rows).to_have_count(5)

row = rows.filter(has_text="CASE-1042")
row.get_by_role("button", name="Edit").click()

names = rows.locator("td:nth-child(2)").all_inner_texts()
assert names == sorted(names)                               # check sorting