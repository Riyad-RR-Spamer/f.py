import os, sys
try:
    __import__("fui").login()
except Exception as e:
    exit(str(e))
