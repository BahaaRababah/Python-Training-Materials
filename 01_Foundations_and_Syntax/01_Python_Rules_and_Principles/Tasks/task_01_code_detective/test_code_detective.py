"""Automated test runner for Task 1: Code Detective."""

import ast
import subprocess
import sys
from pathlib import Path


def run_test():
    target_file = sys.argv[1] if len(sys.argv) > 1 else "code_detective.py"
    target_path = Path(__file__).parent / target_file

    print(f"Running automated test for {target_file}...\n")

    if not target_path.exists():
        print(f"❌ Error: Could not find '{target_file}'. Make sure you are in the correct directory.")
        sys.exit(1)

    # 1. Parse AST to verify docstring and naming conventions
    try:
        source_code = target_path.read_text()
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"❌ Syntax Error Detected:\n   Line {e.lineno}: {e.msg}")
        print("   Hint: Check for illegal variable names (like starting with numbers or using reserved keywords).")
        sys.exit(1)
    except IndentationError as e:
        print(f"❌ Indentation Error Detected:\n   Line {e.lineno}: {e.msg}")
        print("   Hint: In Python, indentation defines code blocks. Remove unnecessary leading spaces.")
        sys.exit(1)

    # Check for module docstring
    docstring = ast.get_docstring(tree)
    if not docstring:
        print("❌ PEP 8 Docstring Missing: The module must have a docstring at the very top explaining its purpose.")
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

    # 3. Verify required outputs
    expected_snippets = [
        "Player: Alex",
        "Class: Mage",
        "Health: 100",
        "Score: 50",
    ]

    for snippet in expected_snippets:
        if snippet not in output:
            print(f"❌ Test Failed: Expected '{snippet}' in output, but got:\n   {output}")
            sys.exit(1)

    # 4. Verify illegal/bad names are not present in source code or AST
    if "1st_player_name" in source_code:
        print("❌ Test Failed: Found illegal variable name starting with a number ('1st_player_name').")
        sys.exit(1)

    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            if node.id == "PlayerScore":
                print("❌ Test Failed: 'PlayerScore' violates PEP 8 snake_case naming for variables.")
                sys.exit(1)
            if node.id in ("class", "def", "if", "for", "import"):
                print(f"❌ Test Failed: '{node.id}' is a reserved keyword and cannot be used as a variable name.")
                sys.exit(1)

    print("✅ All tests passed successfully!")
    print(f"Output received:\n   {output}")


if __name__ == "__main__":
    run_test()
