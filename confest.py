"""
    3. What is conftest.py?
    A special file where shared fixtures and hooks live. pytest finds it automatically, so you never import 
    from it. A conftest.py in a subfolder applies only to tests in that folder, and a root-level one applies to all.
"""

import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "storage_state": "auth/user1.json"}