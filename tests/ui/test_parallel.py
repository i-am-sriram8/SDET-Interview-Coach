"""
    pytest -n 4                                         # parallel with pytest-xdist
    pytest --browser chromium --browser firefox         # cross-browser
    pytest --browser webkit


    Parallel runs need independent tests: unique data per test, 
    no shared accounts mutated by multiple workers, and one context per test.

    pytest-xdist is a highly popular, open-source plugin for the pytest testing framework that enables distributed and parallel test 
    execution. By default, pytest runs your test suite sequentially (one test after another) inside a single process. 
    If you have hundreds or thousands of tests, this can take a long time. pytest-xdist solves this by letting you leverage multiple 
    CPU cores or even remote machines to run tests at the same time

    Trdae-offs when using pytest-xdist


    • State Isolation: Because each worker is a completely separate process, they do not share memory, variables, or global caches.
    • Race Conditions: If your tests read/write to the exact same file path or database row simultaneously, 
    they will conflict and randomly fail (flakiness).
    • Fixture Duplication: A session-scoped fixture (like setting up a test database) will run once per worker process, not once per 
    entire test suite run. If you have 8 workers, it will spin up 8 times unless you implement file-locking mechanisms to restrict it
"""