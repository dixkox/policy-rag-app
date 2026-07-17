print("DEBUG SCRIPT STARTED")

import os, sys, traceback

try:
    print("\n=== CURRENT WORKING DIRECTORY ===")
    print(os.getcwd())

    print("\n=== FILES IN CURRENT DIRECTORY ===")
    print(os.listdir("."))

    print("\n=== PYTHON PATH (sys.path) ===")
    for p in sys.path:
        print(" -", p)

    print("\n=== PROJECT TREE ===")
    for root, dirs, files in os.walk(".", topdown=True):
        level = root.count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

    print("\n=== IMPORT TESTS ===")

    def test(name):
        print(f"\nTrying import: {name}")
        try:
            __import__(name)
            print(f"SUCCESS: {name}")
        except Exception as e:
            print(f"FAILED: {name}")
            print("Error:", e)
            print(traceback.format_exc())

    test("scripts")
    test("scripts.retrieval")
    test("scripts.rag_answer")
    test("app")
    test("app.routes")
    test("app.main")

except Exception as e:
    print("\nFATAL ERROR IN DEBUG SCRIPT:")
    print(e)
    print(traceback.format_exc())

print("\nDEBUG SCRIPT FINISHED")
