"""
DAY-05: cleaned input examples

This module converts the original interactive REPL transcript into a
small, runnable script that demonstrates several common input parsing
patterns while handling invalid input gracefully.

Design goals:
- Avoid unsafe use of `eval`; use `ast.literal_eval` for parsing literals.
- Use `try/except` blocks to handle user input errors (ValueError, SyntaxError).
- Keep helper code small and well-documented to make it suitable for
  beginners studying input handling.
"""

import ast
from typing import Callable, List, Any


def safe_input_list(prompt: str, cast: Callable = str) -> List[Any]:
  """Read a line of input, split on whitespace, and cast each token.

  Returns an empty list when the user provides no input. The `cast`
  argument allows conversion to `int`, `float`, etc.
  """
  data = input(prompt).strip()
  if not data:
    return []
  return [cast(x) for x in data.split()]


def main() -> None:
  """Interactive demo that asks for several values and prints parsed results.

  Each block catches parsing errors and prints a sensible default
  (commonly `None`, `[]`, `()`, or `set()`), keeping the program
  robust for teaching or quick experiments.
  """

  # Basic string input
  name = input("Enter your name: ")
  print("Name:", name)

  # Integer parsing with fallback to None on failure
  try:
    age = int(input("Enter your age: "))
  except ValueError:
    age = None
  print("Age:", age)

  # Float parsing with fallback
  try:
    gpa = float(input("Enter your GPA: "))
  except ValueError:
    gpa = None
  print("GPA:", gpa)

  # Space-separated product names -> list of strings
  products = safe_input_list("Enter the products (space-separated): ")
  print("Products:", products)

  # Topics -> tuple of strings
  topics = tuple(safe_input_list("Enter the topics (space-separated): "))
  print("Topics:", topics)

  # Operators -> set of unique operator names
  op = set(safe_input_list("Enter operators (space-separated): "))
  print("Operators:", op)

  # Marks -> list of ints (empty list on parse error)
  try:
    marks = list(map(int, input("Enter the marks (space-separated): ").split()))
  except ValueError:
    marks = []
  print("Marks:", marks)

  # Prices -> tuple of ints
  try:
    prices = tuple(map(int, input("Enter the prices (space-separated): ").split()))
  except ValueError:
    prices = ()
  print("Prices:", prices)

  # Ratings -> set of ints (duplicates removed)
  try:
    rating = set(map(int, input("Enter ratings (space-separated): ").split()))
  except ValueError:
    rating = set()
  print("Ratings:", rating)

  # Percentages -> list of floats
  try:
    per = list(map(float, input("Enter percentages (space-separated): ").split()))
  except ValueError:
    per = []
  print("Percentages:", per)

  # Demonstrate converting to a tuple of floats
  try:
    price_tuple = tuple(map(float, input("Enter prices for tuple (space-separated): ").split()))
  except ValueError:
    price_tuple = ()
  print("Price tuple:", price_tuple)

  # Demonstrate converting to a set of floats
  try:
    price_set = set(map(float, input("Enter prices for set (space-separated): ").split()))
  except ValueError:
    price_set = set()
  print("Price set:", price_set)

  # Username and password input: split and validate
  creds = input("Enter username and password (space-separated): ").split()
  if len(creds) >= 2:
    username, password = creds[0], creds[1]
  else:
    username = creds[0] if creds else ""
    password = ""
  print("Username:", username)
  print("Password:", password)

  # Read exactly four sides (cast to int). Provide an error message if missing.
  sides = safe_input_list("Enter 4 sides (space-separated): ", int)
  if len(sides) >= 4:
    a, b, c, d = sides[:4]
    print("Sides:", a, b, c, d)
  else:
    print("Sides: not enough values")

  # Price and discount as two floats
  pd = safe_input_list("Enter price and discount (space-separated): ", float)
  if len(pd) >= 2:
    price, discount = pd[0], pd[1]
    print("Price:", price, "Discount:", discount)
  else:
    print("Price/discount: not provided correctly")

  # Safer alternative to eval: parse Python literals using ast.literal_eval
  try:
    literal = input("Enter a Python literal (e.g. [1,2,3] or {'a':1}): ")
    if literal.strip():
      a = ast.literal_eval(literal)
    else:
      a = None
  except (ValueError, SyntaxError):
    a = None
  print("Parsed literal:", a)


if __name__ == "__main__":
  main()