"""
DAY-06 — String methods examples

This file contains short examples demonstrating many commonly used
string methods in Python. Most examples are left commented so you can
uncomment the snippet you want to run while studying.

Sections:
- basic metrics (length, sorting, min/max, ord/chr)
- case methods (upper, lower, title, etc.)
- alignment methods (center, ljust, rjust, zfill)
- search/find methods (find, rfind, index, rindex, count)
- replace/translate (showing str.replace and str.translate usage)
- split/join/partition methods
- encoding example

To run an example, remove the surrounding triple quotes for that
block and execute the file or run the snippet in an interactive
interpreter.
"""

# Basic metrics: length, sorting characters, min/max, ord/chr
'''s = "Rishi varma"
print("Length of characters : ", len(s))
print("Sorting the string is :", sorted(s))
print("Maximum value of character is : ", max(s))
print("Minimum value of character is :", min(s))
print("ASCII value of character 'a' is :", ord('a'))
print("Character from code point 97 is :", chr(97))'''

# Case methods: change letter casing
'''s = "Rishi varma"
print("upper():", s.upper())       # ALL UPPERCASE
print("lower():", s.lower())       # all lowercase
print("title():", s.title())       # Title Case: each word capitalized
print("casefold():", s.casefold()) # aggressive lowercasing for caseless matching
print("swapcase():", s.swapcase()) # swap case of each character'''

# Alignment methods: pad or align text within a given width
'''s = "Rishi varma"
print("center(width, fillchar):", s.center(20, "*"))
print("ljust(width, fillchar):", s.ljust(20, "*"))
print("rjust(width, fillchar):", s.rjust(20, "*"))
print("zfill(width):", s.zfill(50))  # pads numeric strings with leading zeros'''

# Search and find methods: return positions or counts 
'''s = "Rishi varma"
print(s)
print("find('a') -> first index or -1 if not found:", s.find("a"))
print("rfind('a') -> last index or -1 if not found:", s.rfind("a"))
# index() and rindex() raise ValueError if not found (unlike find/rfind)
# print("index('T'):", s.index('T'))
# print("rindex('a'):", s.rindex('a'))
print("count('a') -> occurrences:", s.count("a"))'''

# Replace and translate: replace is simple; translate uses a translation table
'''s = "Rishi varma"
print(s)
print("replace('a','A'):", s.replace("a", "A"))
# Proper translate example using str.maketrans to map characters
trans_table = str.maketrans({'T': '1', 'a': '2'})
print("translate with mapping:", 'Tanuri'.translate(trans_table))'''


# Splitting, joining and partitioning
'''s = "Rishi varma"
print(s)
print("split(','):", s.split(","))
print("split(',', maxsplit=2):", s.split(",", 2))
print("rsplit(',', maxsplit=2):", s.rsplit(",", 2))
print("splitlines():", s.splitlines())
print("'-'.join(s):", '-'.join(s))  # joins characters of the string with '-'
print("partition('#'):", s.partition('#'))
print("rpartition('-'):", s.rpartition('-'))'''

# Encoding example: convert Unicode string to bytes (UTF-8 by default)
s = "Rishi varma 😀"
print(s)

print("encode() -> bytes (UTF-8):", s.encode())