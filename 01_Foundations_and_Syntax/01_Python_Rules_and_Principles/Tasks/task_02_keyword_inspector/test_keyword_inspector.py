"""Automated test runner for Task 2: Keyword Inspector."""

import ast
import keyword
import subprocess
import sys
from pathlib import Path


def run_test():
    target_file = sys.argv[1] if len(sys.argv) > 1 else "keyword_inspector.py"
    target_path = Path(__file__).parent / target_file

    print(f"Running automated test for {target_file}...\n")

    if not target_path.exists():
        print(f"❌ Error: Could not find '{target_file}'. Make sure you are in the correct directory.")
        sys.exit(1)

    # 1. Parse AST to verify docstring and imports
    try:
        source_code = target_path.read_text()
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"❌ Syntax Error Detected:\n   Line {e.lineno}: {e.msg}")
        sys.exit(1)

    # Check for module docstring
    docstring = ast.get_docstring(tree)
    if not docstring:
        print("❌ Docstring Missing: The module must have a docstring at the very top explaining its purpose.")
        sys.exit(1)

    # Check that keyword module is imported
    imported_modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.append(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.append(node.module)

    if "keyword" not in imported_modules:
        print("❌ Test Failed: You must import the 'keyword' module.")
        sys.exit(1)

    # 2. Run the script and capture output
    process = subprocess.run(
        [sys.executable, str(target_path)],
        text=True,
        capture_output=True,
        check=False,
    )

    if process.returncode != 0:
        print("❌ Error: Script execution failed:")
        print(process.stderr)
        sys.exit(1)

    output = process.stdout.strip()
    kw_count = len(keyword.kwlist)

    expected_checks = [
        "--- Python Identifier Inspector ---",
        "user_name -> Valid Identifier: True | Reserved Keyword: False",
        "2nd_place -> Valid Identifier: False | Reserved Keyword: False",
        "class -> Valid Identifier: True | Reserved Keyword: True",
        "MAX_CONNECTIONS -> Valid Identifier: True | Reserved Keyword: False",
        f"Total Reserved Keywords in Python: {kw_count}",
    ]

    for expected in expected_checks:
        if expected not in output:
            print(f"❌ Test Failed: Expected line not found in output:\n   Expected: {expected}\n   Actual Output:\n{output}")
            sys.exit(1)

    print("✅ All tests passed successfully!")
    print(f"Output received:\n{output}")


if __name__ == "__main__":
    run_test()
