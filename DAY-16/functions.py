
def function_name(arg):
    # Example placeholder function: return the argument unchanged.
    return arg

# Example call to the corrected placeholder function.
print(function_name('para'))


def wish(name):
    print(f'Welcome to the python course {name}!')

wish('Ashrutha')
wish('chutkii')
wish('komalatha')
wish('subbu')



def iseven(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-Odd Number"

print(iseven(12))
print(iseven(13))


def factorial(num):
    # Compute factorial using a loop from 1 to num.
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = int(input("Enter the number to compute factorial: "))
print("Factorial:", factorial(num))



def isprime(num):
    # Check if num is a prime number.
    if num < 2:
        return f"{num}-Not prime number"

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num}-Not prime number"
    return f"{num}-prime number"

num = int(input("Enter the number to check prime: "))
print(isprime(num))























