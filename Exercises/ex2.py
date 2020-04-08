"""
Write a Python program to get the Python version you are using.
"""
# method 1
import sys
print(sys.version)

# method 2
from platform import python_version
print(python_version())