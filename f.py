import os, sys
try:
    __import__("abcd").main()
except Exception as e:
    exit(str(e))
