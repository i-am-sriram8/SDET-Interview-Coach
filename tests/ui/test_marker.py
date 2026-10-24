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