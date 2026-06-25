# Built-in module examples: sys, platform, math, and random
# This script demonstrates how Python's built-in modules are used for
# command-line access, system information, math operations, and random values.
# It helps beginners understand why these modules are useful, how they work,
# and how they can support real programs.

import sys

# sys.argv is the list of command-line arguments passed to this script.
# This is useful when you want your script to accept options or file names.
print(sys.argv)  # expected output: list of arguments, e.g. ['built-in.py']

# sys.path lists directories Python searches for imported modules.
# It helps debug import errors and understand module lookup order.
print(sys.path)

# sys.version shows the current Python interpreter version.
# Use this when code depends on Python version differences.
print(sys.version)

print("Before exit")
# sys.exit() terminates the running program immediately.
# Any code below this line will not execute unless sys.exit() is removed.
sys.exit()
print("After exit")  # this print is unreachable because of sys.exit()

# platform is used to query operating system and processor details.
# Note: this block will not run if sys.exit() above is active.
import platform
print(platform.system(), platform.release(), platform.processor())


# math function examples
import math

# math.pi and math.e are common mathematical constants.
print(math.pi)  # expected output: 3.141592653589793
print(math.e)   # expected output: 2.718281828459045

# math.sqrt calculates the square root, math.pow computes powers.
print(math.sqrt(25))  # expected output: 5.0
print(math.pow(2, 5))  # expected output: 32.0

# round() converts a float to the nearest integer.
print(round(20.3))  # expected output: 20
print(round(20.8))  # expected output: 21
print(round(20.5))  # expected output: 20

# math.ceil rounds up, math.floor rounds down.
print(math.ceil(12.3))      # expected output: 13
print(math.ceil(12.000001)) # expected output: 13
print(math.ceil(12.8))      # expected output: 13
print(math.ceil(12.99999))  # expected output: 13

print(math.floor(12.99999)) # expected output: 12
print(math.floor(12.00001)) # expected output: 12
print(math.floor(12.3))     # expected output: 12
print(math.floor(12.8))     # expected output: 12

# math.fabs returns the absolute value, math.factorial returns n!.
print(math.fabs(-12))       # expected output: 12.0
print(math.factorial(5))    # expected output: 120
print(math.gcd(8, 28))      # expected output: 4

# Logarithmic and trigonometric functions.
print(math.log(10, 10))     # expected output: 1.0
print(math.sin(10))         # expected output: sine of 10 radians
print(math.cos(10))         # expected output: cosine of 10 radians
print(math.tan(10))         # expected output: tangent of 10 radians

# Convert between radians and degrees.
print(math.degrees(20))     # expected output: degrees for 20 radians
print(math.radians(20))     # expected output: radians for 20 degrees


# random module examples
import random

# Seed makes the random sequence repeatable for testing or examples.
random.seed(4)
print(random.random())      # expected output: random float in [0.0, 1.0)
print(random.randint(1, 6)) # expected output: random integer from 1 to 6
print(random.uniform(1, 6)) # expected output: random float between 1 and 6

l = ['python', 'java', 'c++', 'HTMl', 'SQL']
print(random.choice(l))      # expected output: one random item from l
print(random.choices(l, k=3))# expected output: list of 3 random items from l

s = 'rps'
print(random.choice(s))      # expected output: one random character from 'rps'
print(l)                     # current list order
random.shuffle(l)            # shuffle list order in place
print(l)                     # expected output: same items but random order

