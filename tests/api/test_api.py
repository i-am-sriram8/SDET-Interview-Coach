from playwright.sync_api import expect
import playwright.sync_api as playwright

api = playwright.request.new_context(
    base_url="https://api.example.com",
    extra_http_headers={"Authorization": f"Bearer {token}"},
)
resp = api.post("/cases", data={"patient_id": 12, "type": "inquiry"})
expect(resp).to_be_ok()     # status 200-299
assert resp.json()["status"] == "open"

"""
    Response codes:

    200 OK
    201 Created (after POST)
    204 No Content (often after DELETE)

    400 Bad Request (malformed input)
    401 Unauthorized (not authenticated)
    403 Forbidden (authenticated but not allowed)
    404 Not Found
    409 Conflict (duplicate or state clash)
    422 Unprocessable Entity (valid format, invalid business data)

    500 Server Error
    502/503 gateway or service unreachable

    Authentication vs Authorization
    Authentication proves identity and authorization decides what you may do. Types: Basic(username and 
    password, base64-encoded, not encrypted), API key(a header or query parameter), Bearer token (Authorizaion: 
    Bearer <token>, typically JWT or OAuth)
"""

"""
    How do you test pagination?
    Check page and limit return the right count, the last page returns the remainder, no record repeats across
    pages, total ount matches, and an out-of-range page returns an empty list or a clear error.

    How do you test an API that depends on another service that isn't ready?
    Use a mock or stub for that dependency, such as a Postman mock server or Wiremock, and add contract checks
    so the mock matches the real service.
"""