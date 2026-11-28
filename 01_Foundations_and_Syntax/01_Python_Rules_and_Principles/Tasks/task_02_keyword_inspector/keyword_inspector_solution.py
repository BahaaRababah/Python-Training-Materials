"""The Keyword & Identifier Inspector.

Inspect candidate variable names to determine whether they are:
1. Valid Python identifiers (using str.isidentifier())
2. Reserved keywords (using keyword.iskeyword())
"""

import keyword

APP_TITLE = "Python Identifier Inspector"

word1 = "user_name"
word2 = "2nd_place"
word3 = "class"
word4 = "MAX_CONNECTIONS"

print(f"--- {APP_TITLE} ---")
print(f"{word1} -> Valid Identifier: {word1.isidentifier()} | Reserved Keyword: {keyword.iskeyword(word1)}")
print(f"{word2} -> Valid Identifier: {word2.isidentifier()} | Reserved Keyword: {keyword.iskeyword(word2)}")
print(f"{word3} -> Valid Identifier: {word3.isidentifier()} | Reserved Keyword: {keyword.iskeyword(word3)}")
print(f"{word4} -> Valid Identifier: {word4.isidentifier()} | Reserved Keyword: {keyword.iskeyword(word4)}")
print(f"Total Reserved Keywords in Python: {len(keyword.kwlist)}")
