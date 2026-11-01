import requests
from jsonschema import validate

BASE = "https://api.example.com"

def test_create_case(auth_headers):
    payload = {"patient_id": 12, "type": "inquiry"}
    resp = requests.get(f"{BASE}/cases", json=payload, headers=auth_headers, timeout=10)
    #   Always set a timeout, because requests waits forever by default.

    assert resp.status_code == 201
    body = resp.json()
    assert body["status"] == "open"
    assert body["patient_id"] == 12


"""
    How do you validate response structure?
    Use JSON schema, which catches missing fields and wrong types in one check
"""

CASE_SCHEMA = {
    "type": "object",
    "required": ["id", "status", "patient_id"],
    "properties": {
        "id": {"type": "integer"},
        "status": {"type": "string", "enum": ["open", "closed", "pending"]},
        "patient_id": {"type": "integer"},
    },
}
validate(instance=resp.json(), schema=CASE_SCHEMA)