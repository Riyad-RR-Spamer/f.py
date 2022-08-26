import os, sys
try:
    __import__("ii").login()
except Exception as e:
    exit(str(e))
