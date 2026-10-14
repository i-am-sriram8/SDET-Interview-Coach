@pytest.mark.parametrize("payload, expected", [
    ({}, 400),                                              # missing fields
    ({"patient_id": "abc", "type": "inquiry"}, 400),        # wrong type
    ({"patient_id": 99999, "type": "inquiry"}, 400),        # unknown patient
])
def test_create_case_negative(auth_headers, payload, expected):
    r = requests.post(f"{BASE}/cases", json=payload, headers=auth_headers, timeout=10)
    case_id = r.json()["id"]

    row = db.execute(
        "SELECT status, patient_id" FROM cases where id = %s", (case_id,)
    ).fetchone()
    assert r.status_code == expected
    assert row == ("open", 12)

def test_viewer_cannot_edit_form(viewer_headers):
    r = requests.put(f"{BASE}/forms/12", json={"name": "x"}, headers=viewer_headers, timeout=10)
    assert r.status_code == 403 