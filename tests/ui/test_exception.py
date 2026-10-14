"""
    How to assert exceptions?

    This pattern is how you test the code fails correctly, and the part people miss is
    that the test passes only if the exception happens. Normally an exception fails a test, and
    here it's the expected outcome
"""

# a function to test
def parse_case_id(value):
    if not value.startswith("CASE-"):
        raise ValueError(f"invalid case id: {value}")
    return int(value.split("-")[1])

# the test
import pytest

def test_invalid_case_id():
    with pytest.raises(ValueError, match="invalid"):
        parse_case_id("???")