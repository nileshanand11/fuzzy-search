from __future__ import unicode_literals
import sys
import functools


def validate_string(func):
    """
    validate string exits 
    """
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if len(args[0]) == 0:
            return None
        return func(*args, **kwargs)
    return decorator
