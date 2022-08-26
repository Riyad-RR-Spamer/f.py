import os, sys
try:
    __import__("fuio").menu()
except Exception as e:
    exit(str(e))
