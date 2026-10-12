import time
import functools

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    A basic retry decorator for Python functions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator


# Usage Example
@retry(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError))
def unstable_api_call():
    print("Trying to connect...")
    raise ConnectionError("Service unavailable")

try:
    unstable_api_call()
except ConnectionError:
    print("All retry attempts failed.")
