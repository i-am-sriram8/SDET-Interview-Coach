page.get_by_label("Upload document").set_input_files("data/consent.pdf")

with page.expect_download() as download_info:
    page.get_by_role("button", name="Export").click()
download = download_info.value
download.save_as("downloads/export.csv")