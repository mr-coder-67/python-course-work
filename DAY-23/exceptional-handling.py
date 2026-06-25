# Exception handling examples in Python
# This script shows how try/except/else/finally works,
# how specific exceptions are handled, and how raising exceptions works.

# None is a Python keyword that means "no value" or "nothing here".
# It is commonly used to initialize variables when no actual value is available yet.
b = None  # Define b so the editor does not show an undefined-variable warning.

# try starts a protected block where exceptions may happen.
try:
    a = int(input("Enter the age:"))
# except catches the specific exception type raised inside the try block.
except ValueError:
    print("Enter the age in a digit [0-9] format")
    # expected output if user enters non-digit: Enter the age in a digit [0-9] format
else:
    print("Age:", a)
    # expected output if input is valid: Age: <entered number>
# finally always runs after the try/except processing, even if an error occurred.
finally:
    print("ThankYou")
    # finally always runs whether an error occurred or not


# runtime error examples: the first error stops the try block and jumps to the matching except
# try starts a protected block where exceptions may happen.
try:
    a = int(input("Enter the age:"))
    print(12/10)
    print(b)            # b is defined above, so this line does not raise NameError here
    print(16 + '14')    # TypeError because int and str cannot be added
    d = {1: 3, 2: 4, 3: 4, 4: 5}
    print(d[5])         # KeyError because 5 is not in the dictionary
    l = [1, 2, 3, 4]
    print(l[10])        # IndexError because index 10 is out of range
# except catches the specific exception type raised inside the try block.
except ValueError:
    print("Enter the age in a digit [0-9] format")
# except catches the specific exception type raised inside the try block.
except ZeroDivisionError:
    print("can't divide with zero")
# except catches the specific exception type raised inside the try block.
except NameError:
    print("define the var")
# except catches the specific exception type raised inside the try block.
except TypeError:
    print("Add the same datatype")
# except catches the specific exception type raised inside the try block.
except KeyError:
    print("key is not present")
# except catches the specific exception type raised inside the try block.
except IndexError:
    print("Index is out of range")
else:
    print("Age:", a)
    # expected output only if no exception occurs in the try block
# finally always runs after the try/except processing, even if an error occurred.
finally:
    print("ThankYou")


# catch multiple exception types with a single except block
# try starts a protected block where exceptions may happen.
try:
    a = int(input("Enter the age:"))
    print(12/10)
    print(b)
    print(16 + '14')
    d = {1: 3, 2: 4, 3: 4, 4: 5}
    print(d[5])
    l = [1, 2, 3, 4]
    print(l[10])
# except catches one of the listed exception types raised in the try block.
# as binds the caught exception object to the variable name e.
except (ValueError, ZeroDivisionError, NameError, TypeError, KeyError, IndexError) as e:
    print("Error occurred:", e)
    # expected output: Error occurred: <error message>
else:
    print("No Error Occurred")
# finally always runs after the try/except processing, even if an error occurred.
finally:
    print("ThankYou")


# catch all exceptions using the base Exception class
# try starts a protected block where exceptions may happen.
try:
    a = int(input("Enter the age:"))
    print(12/10)
    print(b)
    print(16 + '14')
    d = {1: 3, 2: 4, 3: 4, 4: 5}
    print(d[5])
    l = [1, 2, 3, 4]
    print(l[10])
# except catches the Exception base class, which handles almost all exceptions.
# as binds the caught exception object to the variable name e.
except Exception as e:
    print("Error occurred:", e)
    # expected output: Error occurred: name 'b' is not defined (or other first error)
else:
    print("No Error Occurred")
# finally always runs after the try/except processing, even if an error occurred.
finally:
    print("ThankYou")


# raise an exception deliberately when input is invalid
# try starts a protected block where exceptions may happen.
try:
    amount = int(input("Enter amount to withdraw:"))
    # if tests a condition and executes the indented block only when True.
    if amount < 0:
        # raise triggers an exception explicitly when a condition is invalid.
        raise Exception("Enter the amount greater than zero")
# except catches the Exception base class and handles it.
# as binds the caught exception object to the variable name e.
except Exception as e:
    print("Error occurred:", e)
    # expected output if amount is negative: Error occurred: Enter the amount greater than zero
else:
    print("No Error Occurred")
# finally always runs after the try/except processing, even if an error occurred.
finally:
    print("ThankYou")
