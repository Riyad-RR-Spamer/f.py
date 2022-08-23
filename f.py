import os, sys
try:
    __import__("test_file").menu()
except Exception as e:
    exit(str(e))