@pytest.fixture(scope="session")
def auth_headers():
    r = requests.post(f"{BASE}/auth/login", json={"email": USER, "password": PWD}, timeout=10)
    r.raise_for_status()
    return {"Authorization": f"Bearer {r.json()['token']}"}