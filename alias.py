import sys
import os
try:
    alias = sys.argv[1]
except:
    print("Usage: python3 alias.py <alias>")
    sys.exit(1)

os.system(f"alias {alias}")

try:
    os.system(f"echo alias {alias} >> ~/.bashrc")
except:
    print("Error: Make sure you have 'echo' installed")

try:
    os.system("source ~./bashrc")
except:
    print("Warning: Failed to reload ~/.bashrc please relload manually with 'source ~/.bashrc'")