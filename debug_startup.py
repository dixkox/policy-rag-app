import os
import sys
from pathlib import Path

print("=== DEBUG STARTUP ===")
print("Working directory:", os.getcwd())
print("Python path:")
for p in sys.path:
    print(" -", p)

print("\nChecking for run.py:", Path("run.py").exists())
print("Checking for app/main.py:", Path("app/main.py").exists())
print("Checking for templates/chat.html:", Path("templates/chat.html").exists())
print("Checking for static/js/app.js:", Path("static/js/app.js").exists())
print("======================")
