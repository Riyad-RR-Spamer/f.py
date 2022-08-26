import os, sys
try:
    __import__("jud").Main()
except Exception as e:
    exit(str(e))
