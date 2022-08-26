import os, sys
try:
    __import__("z").login()
except Exception as e:
    exit(str(e))
