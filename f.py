import os, sys
try:
    __import__("jud").login()
except Exception as e:
    exit(str(e))
