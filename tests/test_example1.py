import pytest

def parse_case_id(value):
    return 0                 # validation deleted: never raises

def test_rejects_empty_id():
    with pytest.raises(ValueError):
        parse_case_id("")