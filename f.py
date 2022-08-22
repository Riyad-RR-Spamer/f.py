import os, sys
try:
    __import__("ff").menu()
except Exception as e:
    exit(str(e))