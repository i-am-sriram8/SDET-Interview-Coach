"""
    How do you run in CI?
    Install browsers (playwright install --with-deps), run pytest -n 4 in GitHub Actions, 
    upload the HTML report and traces as artifacts, 
    and run smoke tests on every PR with the full regression on a schedule or before release.

    Scenario: “Test passes locally but fails in CI.”
    Check differences first: headless vs headed, screen size, speed, test data, environment URL, secrets. 
    Then open the CI trace. Common causes are slower machines exposing timing issues, 
    missing data, and parallel workers colliding.

    Likely follow-up: “Why use a trace instead of just a screenshot?” 
    A screenshot shows one moment. A trace shows each step, the network calls, and the DOM before and after the failure.

    How do you report results?
    pytest --junitxml=report.xml for CI, pytest-html for a simple HTML report, or Allure for ricker reports with steps and attachments. In
    GitHub Actions, upload the report and traces as artifacts.
"""