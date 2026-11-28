"""The Keyword & Identifier Inspector.

Inspect candidate variable names to determine whether they are:
1. Valid Python identifiers (using str.isidentifier())
2. Reserved keywords (using keyword.iskeyword())
"""

# Step 1: Import the built-in 'keyword' module
# import ...

# Step 2: Define a constant for the inspector banner in UPPER_SNAKE_CASE
# APP_TITLE = "Python Identifier Inspector"

# Step 3: Candidate variable names to evaluate:
word1 = "user_name"
word2 = "2nd_place"
word3 = "class"
word4 = "MAX_CONNECTIONS"

# Step 4: Print the banner and check each word using:
#   - word.isidentifier()
#   - keyword.iskeyword(word)
# And print the total count of reserved keywords using len(keyword.kwlist).
#
# Expected output format:
# --- Python Identifier Inspector ---
# user_name -> Valid Identifier: True | Reserved Keyword: False
# 2nd_place -> Valid Identifier: False | Reserved Keyword: False
# class -> Valid Identifier: True | Reserved Keyword: True
# MAX_CONNECTIONS -> Valid Identifier: True | Reserved Keyword: False
# Total Reserved Keywords in Python: <count>
