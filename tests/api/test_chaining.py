import pytest
import requests


@pytest.fixture(scope="session")
def auth_headers():
    r = requests.post(f"{BASE}/auth/login", json={"email": USER, "password": PWD}, timeout=10)
    r.raise_for_status()
    return {"Authorization": f"Bearer {r.json()['token']}"}

"""
    Chaining is just passing a value forward: create a case, take body["id"], then GET /cases/{id}.
    Clean up created data in fixture teardown.
"""