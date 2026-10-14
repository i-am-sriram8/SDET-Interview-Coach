"""
    1. What is a fixture, and why use it instead of setup/teardown?
    A fixture is a reusable function that prepares something a test needs, such as a logged-in page or test data. 
    Tests request it by naming it as a parameter, and pytest injects it. Code after yield is the teardown.
"""
import pytest

@pytest.fixture
def case_date():
    case_id = create_case_via_api()     # setup
    yield case_id                       # test runs here
    delete_case_via_api(case_id)        # runs even if the test fails


"""
    It beats xUnit-style setup because it’s composable, requested only by the tests that need it, 
    and each fixture owns its own cleanup.
"""


def test_case_status(page, case_data):
    page.goto(f"/cases/{case_data}")


"""
    2. What are fixture scopes?
    function (default, runs per test), class, module, package, session (once per run).

    Trade-off: a wider scope is faster but weakens isolation. Use function for anything a test mutates, 
    such as pages, contexts, and data. Use session for expensive, read-only things such as tokens or config.

"""
@pytest.fixture(scope="session")
def api_token():
    return login_and_get_token()


"""
    3. What is conftest.py?
    A special file where shared fixtures and hooks live. pytest finds it automatically, so you never import 
    from it. A conftest.py in a subfolder applies only to tests in that folder, and a root-level one applies to all.
"""

"""
    marker: label only, used for selection

    parametrize: one function, multiple runs with different data

    How do you stop a typo like @pytest.mark.smok from silently passing?” Register markers in pytest.ini and 
    use --strict-markers, so unknown markers raise an error.
"""


@pytest.mark.parametrize("role, can_edit", [
    ("physician", True),
    ("viewer", False),
])
def test_form_edit_permission(role, can_edit):
    assert check_edit_permission(role) == can_edit