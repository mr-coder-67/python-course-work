# Operator examples in Python

# Initialize two integer variables for examples
a = 20
b = 30

# Arithmetic operators
# + addition, - subtraction, * multiplication, / division
# // integer division, ** exponentiation, % remainder
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =', a // b)
print('a ** 3 =', a ** 3)
print('a % b =', a % b)

# Comparison operators
# > greater than, < less than, >= greater than or equal to,
# <= less than or equal to, == equal to, != not equal to
print('a > b ->', a > b)
print('a < b ->', a < b)
print('a >= b ->', a >= b)
print('a <= b ->', a <= b)
print('a == b ->', a == b)
print('a != b ->', a != b)

# Assignment operators
# Standard assignment and compound assignment operators
y = 5
print('\ny =', y)

y = y + 5
print('y = y + 5 ->', y)

y = 5
print('\ny =', y)
y += 10  # same as y = y + 10
print('y += 10 ->', y)
y -= 10  # same as y = y - 10
print('y -= 10 ->', y)
y *= 2  # same as y = y * 2
print('y *= 2 ->', y)
y /= 5  # same as y = y / 5 (float result)
print('y /= 5 ->', y)
y //= 2  # same as y = y // 2
print('y //= 2 ->', y)
y **= 3  # same as y = y ** 3
print('y **= 3 ->', y)

# Logical operators
# and, or, not combine boolean expressions
print('\na % 10 == 0 ->', a % 10 == 0)
print('a % 20 == 0 and b % 20 == 0 ->', a % 20 == 0 and b % 20 == 0)
print('a % 20 == 0 or b % 20 == 0 ->', a % 20 == 0 or b % 20 == 0)
print('not a > b ->', not a > b)

# Membership operators
# in checks whether an item exists in a sequence or collection
# not in checks whether an item does not exist
text = 'python programming'
print('\n"y" in text ->', 'y' in text)
print('"g" not in text ->', 'g' not in text)
print('"r" not in text ->', 'r' not in text)

languages = ['java', 'python', 'mysql', 'c++', 'html']
print('\n"java" in languages ->', 'java' in languages)
print('"javascript" not in languages ->', 'javascript' not in languages)
print('"mqsql" not in languages ->', 'mqsql' not in languages)

numbers = {1, 2, 3, 4, 5, 6}
print('\n5 in numbers ->', 5 in numbers)
print('5 not in numbers ->', 5 not in numbers)

prices = {'oil': 29, 'sugar': 234, 'tea': 345}
print('\n"oil" in prices ->', 'oil' in prices)
print('"tea" not in prices ->', 'tea' not in prices)

# Identity operators
# is checks whether two names refer to the same object
m = [1, 2, 3, 4, 5]
n = m
print('\nm == n ->', m == n)  # same values
print('m is n ->', m is n)  # same object

# Bitwise operators
# & bitwise AND, | bitwise OR, ^ bitwise XOR
# ~ bitwise NOT, >> right shift, << left shift
print('\n8 & 14 ->', 8 & 14)
print('8 | 7 ->', 8 | 7)
print('10 ^ 11 ->', 10 ^ 11)
print('~12 ->', ~12)
print('15 >> 3 ->', 15 >> 3)
print('13 << 6 ->', 13 << 6)
print('16 << 1 ->', 16 << 1)

# Print formatting example with f-string
c = 'python'
print('\nFormatted output:')
print(f'a = {a}, b = {b}, c = {c}')
