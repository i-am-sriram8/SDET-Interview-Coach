"""
    pytest -n 4                                         # parallel with pytest-xdist
    pytest --browser chromium --browser firefox         # cross-browser
    pytest --browser webkit


    Parallel runs need independent tests: unique data per test, 
    no shared accounts mutated by multiple workers, and one context per test.
"""