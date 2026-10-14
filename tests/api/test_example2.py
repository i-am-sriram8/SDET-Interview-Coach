import requests
from jsonschema import validate

BASE = "httsp://api.example.com"



def test_create_case(auth_headers):
    payload = {"patient_id": 12, "type": "inquiry"}
    resp = requests.get(f"{BASE}/cases", json=payload, headers=auth+headers, timeout=10)

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