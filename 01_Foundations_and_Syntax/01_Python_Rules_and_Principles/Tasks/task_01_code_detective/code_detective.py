# code_detective.py
# ==============================================================================
# TASK 1: THE CODE DETECTIVE (Fix Syntax, PEP 8 & Naming Violations)
# ==============================================================================
# A teammate wrote this configuration script for a game character, but it is
# full of syntax errors, illegal identifier names, bad indentation, and PEP 8
# violations.
#
# YOUR MISSION:
# 1. Add a module-level docstring at the very top of the file describing its purpose.
# 2. Fix the illegal identifier starting with a number:
#      Change `1st_player_name = "Alex"` to `player_name = "Alex"`.
# 3. Fix the reserved keyword error:
#      `class = "Mage"` cannot be used because 'class' is a reserved keyword!
#      Rename it to `character_class = "Mage"`.
# 4. Enforce PEP 8 naming for the constant:
#      `max_health = 100` is intended as a constant.
#      Rename it to `MAX_HEALTH = 100`.
# 5. Enforce PEP 8 naming for standard variables:
#      `PlayerScore = 50` is PascalCase. Variables must use snake_case:
#      Rename it to `player_score = 50`.
# 6. Fix the indentation error:
#      Python does not allow random indentation. Remove unnecessary leading spaces.
# 7. Print the character stats formatted as shown below:
#      Player: Alex | Class: Mage | Health: 100 | Score: 50
# ==============================================================================

# FIXME 1: Add a module docstring at the top of this file

# FIXME 2: Fix syntax error (variable names cannot start with a number)
1st_player_name = "Alex"

# FIXME 3: Fix syntax error ('class' is a reserved Python keyword)
class = "Mage"

# FIXME 4: Constants must follow PEP 8 UPPER_SNAKE_CASE
max_health = 100

# FIXME 5: Standard variables must follow PEP 8 snake_case (not PascalCase)
PlayerScore = 50

# FIXME 6: Fix indentation error (remove unintended leading whitespace)
    is_active = True

# FIXME 7: Print the character stats
# Expected output format:
# Player: Alex | Class: Mage | Health: 100 | Score: 50
