"""
    Playwright auto-dismisses dialogs if there's no handler.
"""


# page.once: handles only the next dialog
page.once("dialog", lambda dialog: dialog.dismiss()) 
page.get_by_role("button", name="Delete").click()  # dismissed
page.get_by_role("button", name="Archive").click() # no handler now, so playwright auto-dismisses


# page.on: handles every dialog on this page until removed
def accept_dialog(dialog):
    dialog.accept()

page.on("dialog", accept_dialog)
page.get_by_role("button", name="Delete").click()   # accepted
page.get_by_role("button", name="Archive").click()  # also accepted

page.remove_listener("dialog", accept_dialog)       # remove
page.get_by_role("button", name="Delete").click()   # no handler now, so auto-dismissed  