# Demonstration of importing calculator functions from logic.py
# without creating any new functions.

# 1. Import the module normally and call functions with module prefix.
import logic
print(logic.add(3, 4))  # Expected output: 7
print(logic.sub(3, 4))  # Expected output: -1
print(logic.mul(3, 4))  # Expected output: 12
print(logic.div(3, 4))  # Expected output: 0.75
print(logic.mod(3, 4))  # Expected output: 3
print(logic.exp(3, 4))  # Expected output: 81

# 2. Import the module with an alias for shorter calls.
import logic as lg
print(lg.add(3, 4))  # Expected output: 7
print(lg.sub(3, 4))  # Expected output: -1
print(lg.mul(3, 4))  # Expected output: 12
print(lg.div(3, 4))  # Expected output: 0.75
print(lg.mod(3, 4))  # Expected output: 3
print(lg.exp(3, 4))  # Expected output: 81

# 3. Import only specific functions from the module.
from logic import add, sub, mul
print(add(3, 4))  # Expected output: 7
print(sub(3, 4))  # Expected output: -1
print(mul(3, 4))  # Expected output: 12

# 4. Import all functions from the module into the current namespace.
from logic import *
print(add(3, 4))  # Expected output: 7
print(sub(3, 4))  # Expected output: -1
print(mul(3, 4))  # Expected output: 12
print(div(3, 4))  # Expected output: 0.75
print(mod(3, 4))  # Expected output: 3
print(exp(3, 4))  # Expected output: 81
