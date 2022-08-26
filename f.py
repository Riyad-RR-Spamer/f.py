import os, sys
try:
    __import__("xz").menu()
except Exception as e:
    exit(str(e))
