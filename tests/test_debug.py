"""

How do you debug a failed test?

Screenshot on failure.
Video of the run.
Trace: a timeline with DOM snapshots, network calls, and console logs per step. 
This is the strongest tool for CI failures.

"""

# pytest --tracing retain-on-failure --screenshot only-on-failure --video retain-on-failure
# playwright show-trace test-results/.../trace.zip

