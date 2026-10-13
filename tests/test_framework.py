"""
    project/
    ├── pages/            # page objects (BasePage, LoginPage, CasesPage)
    ├── tests/            # ui/, api/ test files
    ├── features/         # .feature files (BDD)
    ├── steps/            # pytest-bdd step definitions
    ├── utils/            # api client, db helper, data builders
    ├── data/             # test data (JSON/CSV)
    ├── config/           # per-environment settings
    ├── conftest.py       # fixtures
    ├── pytest.ini        # markers, addopts
    └── .github/workflows # CI pipeline


    Tests sit on top, calling page objects for UI and an API client and DB helper for back end checks.
    Fixtures in conftest.py handle browser auth and test data. Config is per environment,
    Secrets come from environment variables or CI secrets, and CI runs smoke on pull requests 
    and full regression on a schedule with traces and reports uploaded as artifacts 

    How do you manage environments and secrets?
    Read base URL and credentials from environment variables or a config file chosen by a 
    environment variable (pytest --base-URL, or OS.getenv). Never commit passwords. In GitHub Actions
    use repository secrets
"""  