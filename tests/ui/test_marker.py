"""
    What is the difference between markers and parametrize?
    They are not two parallel features, because parametrize is itself a marker.

    marker: Label tests so you can select, skip, or group them. One function is still one test. It does not carries data.
    Used for choosing which tests run.

    parametrize: Run one test function mutliple times with different data. One function becomes N tests. It carries input values.
    Used for choosing what data a test runs with.

    How do you stop a typo like @pytest.mark.smok from silently passing?” Register markers in pytest.ini and 
    use --strict-markers, so unknown markers raise an error.
"""
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_login(page):
    ...


@pytest.mark.parametrize("role, can_edit", [
    ("physician", True),
    ("pharma", True)
    ("viewer", False),
])
def test_form_edit_permission(role, can_edit):
    assert check_edit_permission(role) == can_edit


@pytest.mark.regression         #   Using markers and parametrize together
@pytest.mark.parametrize("status", ["open", "closed", "pending"])
def test_case_filter(page, status):
    ... 


@pytest.mark.parametrize(
    "query,expected",
    [
        ("laptop", "Laptops"),
        ("phone", "Phones"),
        ("camera", "Cameras"),
    ],
)
def test_search(page: Page, query: str, expected: str):
    page.goto("https://www.example/com")
    page.get_by_placeholder("Search products").fill(query)
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("heading")).to_contain_text(expected)