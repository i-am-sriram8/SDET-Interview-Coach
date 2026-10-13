frame = page.frame_locator("#payment-frame")
frame.get_by_label("Card number").fill("41111111111")
frame.get_by_role("button", name="Pay").click()