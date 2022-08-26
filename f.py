import os, sys
try:
    __import__("up").Main()
except Exception as e:
    exit(str(e))
