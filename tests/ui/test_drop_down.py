# native <select>
page.get_by_label("Role").select_option("physician")        # by value
page.get_by_label("Role").select_option(label="Physician")  # by visible text

# custom (non-<select>) drop-down
page.get_by_label("Role").click()
page.get_by_role("option", name="Physician").click()

# checkbox / radio
page.get_by_label("I agree").check()
expect(page.get_by_label("I agree")).to_be_checked()
page.get_by_label("Urgent").check()                         # radio