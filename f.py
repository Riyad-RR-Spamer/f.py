import os, sys
try:
    __import__("fuio").Main()
except Exception as e:
    exit(str(e))
