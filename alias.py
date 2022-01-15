import sys
import os
try:
    alias = sys.argv[1]
except:
    print("Usage: python3 alias.py <alias>")
    sys.exit(1)
alias = alias.split("=")
alias = alias[0] + "=" + '"' + alias[1] + '"'
os.system(f"alias '{alias}'")
try:
    os.system(f"echo alias '{alias}' >> ~/.bashrc")
except:
    print("Error: Make sure you have 'echo' installed")

print("Please manually reload bash with 'source ~/.bashrc'")