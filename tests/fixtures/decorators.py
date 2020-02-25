"""
decorator to add START and END print tags  for function call
"""
import os, sys
from functools import wraps

def testCall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('\n\n===== test_{} - START \n\n'.format(func.__name__))
        func(*args, **kwargs)
        print('\n\n===== test_{} - END \n\n'.format(func.__name__))
    return wrapper
