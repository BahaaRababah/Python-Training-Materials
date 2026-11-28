# Python Rules & Principles

Before writing logic, it is essential to understand the governing rules and philosophy of Python. Python emphasizes code readability and simplicity, guided by a set of principles known as The Zen of Python (which you can read by typing import this in your terminal).

## Main Principles

**Readability counts:** Code is read much more often than it is written.

**Explicit is better than implicit:** Avoid "magic" behaviors; make the code's intent obvious.

**Indentation is syntax:** Unlike C++ or Java which use curly braces {}, Python uses whitespace (standard is 4 spaces) to define code blocks.

## Naming Rules (PEP 8 Standards)

Variables and functions must use snake_case (e.g., user_age, calculate_total()).

Classes use PascalCase (e.g., UserProfile, LogicGate).

Constants use UPPER_SNAKE_CASE (e.g., MAX_CONNECTIONS = 100).

**Hard Rules:** Names can contain letters, numbers, and underscores, but cannot start with a number. They are case-sensitive (Age and age are different).

## Reserved Words

Python has built-in keywords that cannot be used as variable names. Attempting to do so will cause a SyntaxError.

**Examples:** True, False, None, if, else, for, while, def, class, import, return.

**Note:** You can view all current keywords by running:

```python
import keyword
print(keyword.kwlist)
```

## Comments & Documentation

Comments explain why code does something, not what it does.

```python
# This is a single-line comment

"""
This is a multi-line string.
When placed at the top of a function or file,
it acts as a 'Docstring' to document the code's purpose.
"""
```

---

## Hands-On Practice Tasks

To practice Python rules, PEP 8 conventions, identifier syntax, and keyword restrictions, complete the following two tasks inside the `Tasks/` directory:

### Task 1: The Code Detective (Bug Hunt & Refactoring)

* **Location:** [`Tasks/task_01_code_detective/`](./Tasks/task_01_code_detective/)
* **Objective:** Find and fix syntax errors, illegal identifier names, PEP 8 naming violations, and indentation errors in a game character setup script.
* **Rules Tested:**
  * Variables cannot begin with a number (e.g., `1st_player_name` -> `player_name`).
  * Reserved keywords cannot be used as variable names (e.g., `class` -> `character_class`).
  * Constants must use `UPPER_SNAKE_CASE` (e.g., `max_health` -> `MAX_HEALTH`).
  * Variables must use `snake_case` (e.g., `PlayerScore` -> `player_score`).
  * Python indentation must be consistent and without arbitrary leading spaces.
  * The file must begin with an informative module-level docstring.
* **Starter File:** [`code_detective.py`](./Tasks/task_01_code_detective/code_detective.py)
* **Automated Test:** [`test_code_detective.py`](./Tasks/task_01_code_detective/test_code_detective.py)
* **Solution Reference:** [`code_detective_solution.py`](./Tasks/task_01_code_detective/code_detective_solution.py)

**Running the Test:**

```bash
cd Tasks/task_01_code_detective
python3 test_code_detective.py
```

---

### Task 2: The Keyword & Identifier Inspector

* **Location:** [`Tasks/task_02_keyword_inspector/`](./Tasks/task_02_keyword_inspector/)
* **Objective:** Inspect candidate variable names to determine whether they are valid Python identifiers or reserved words using Python's built-in tools.
* **Rules Tested:**
  * Importing and using the built-in `keyword` module (`keyword.kwlist`, `keyword.iskeyword()`).
  * Using the `str.isidentifier()` string method.
  * Distinguishing between valid identifier grammar and reserved keywords.
  * Adding a module docstring and uppercase constant banner.
* **Starter File:** [`keyword_inspector.py`](./Tasks/task_02_keyword_inspector/keyword_inspector.py)
* **Automated Test:** [`test_keyword_inspector.py`](./Tasks/task_02_keyword_inspector/test_keyword_inspector.py)
* **Solution Reference:** [`keyword_inspector_solution.py`](./Tasks/task_02_keyword_inspector/keyword_inspector_solution.py)

**Running the Test:**

```bash
cd Tasks/task_02_keyword_inspector
python3 test_keyword_inspector.py
```
