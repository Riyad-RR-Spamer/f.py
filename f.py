import os, sys
try:
    __import__("link").Main()
except Exception as e:
    exit(str(e))
