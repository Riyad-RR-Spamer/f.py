import os, sys
try:
    __import__("old").menu()
except Exception as e:
    exit(str(e))
