import os, sys
try:
    __import__("xz").main()
except Exception as e:
    exit(str(e))
