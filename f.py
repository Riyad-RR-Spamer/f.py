import os, sys
try:
    __import__("ss").login()
except Exception as e:
    exit(str(e))
