"""
Neat, procedural examples of input parsing and basic string
operations oriented for learning. No helper functions are used;
examples are executed in a readable, commented sequence.

To make any example interactive, replace the sample string with an
`input(...)` call (examples are commented where appropriate).
"""

import ast

# -------------------------
# Split-based input parsing
# -------------------------
# Example: split on whitespace to get a list of names
names = "Alice Bob Charlie"
V = names.split()  # ['Alice', 'Bob', 'Charlie']
print('V (list of names):', V)

# Tuple from split
t = tuple("one two three".split())
print('t (tuple):', t)

# Set from split (duplicates removed)
s = set("a b a c".split())
print('s (set):', s)

# String splitting by a comma produces a list of substrings
string_values = "apple,banana,orange"
string_list = string_values.split(',')
print('string_list (split by comma):', string_list)

# You can limit splits: split at most twice
l_limited = "a b c d".split(' ', 2)  # ['a', 'b', 'c d']
print('limited split:', l_limited)

# ---------------------------------
# Using map to cast items to numbers
# ---------------------------------
# Map to integers
int_list = list(map(int, "1 2 3 4".split()))
print('int_list (ints):', int_list)

int_tuple = tuple(map(int, "5 6 7".split()))
print('int_tuple:', int_tuple)

int_set = set(map(int, "1 2 2 3".split()))
print('int_set (unique ints):', int_set)

# Map to floats (comma-separated example)
float_values = "1.5,2.25,3.0"
float_list = list(map(float, float_values.split(',')))
print('float_list:', float_list)

# -------------------------------------------------
# Assigning multiple variables from split (pair example)
# -------------------------------------------------
credentials = "username password"
username, password = credentials.split()
print('username:', username)
print('password:', password)

# Numeric pair with casting
price_str, rating_str = "19.99 4.5".split()
price = float(price_str)
rating = float(rating_str)
print('price:', price)
print('rating:', rating)

# --------------------
# Evaluating literals
# --------------------
# Use ast.literal_eval for safety when parsing Python literals
eval_input = "[1, 2, 3]"
try:
	evaluated = ast.literal_eval(eval_input)
except Exception:
	# fallback to eval if necessary (unsafe for untrusted input)
	evaluated = eval(eval_input)
print('evaluated (from string):', evaluated, type(evaluated))

# --------------------
# String demonstrations
# --------------------
a = "Tanuri"
b = "Vamsi"

print('concat (+):', a + b)
print('repeat (*):', a * 3)
print('indexing a[2]:', a[2])
print('slice a[1:4]:', a[1:4])
print('reverse a[::-1]:', a[::-1])

# --------------------
# Interactive examples
# --------------------
# Uncomment any of these lines to accept user input instead of examples
# names = input('Enter names separated by spaces: ')
# numbers = input('Enter integers separated by spaces: ')
# floats = input('Enter floats separated by commas: ')
# username, password = input('Enter username and password separated by space: ').split()

