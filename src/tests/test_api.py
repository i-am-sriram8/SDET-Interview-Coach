api = playwright.request.new_context(
    base_url="https://api.example.com",
    extra_http_headers={"Authorization": f"Bearer {token}"},
)
resp = api.post("/cases", data={"patient_id": 12, "type": "inquiry"})
expect(resp).to_be_ok()     # status 200-299
assert resp.json()["status"] == "open"