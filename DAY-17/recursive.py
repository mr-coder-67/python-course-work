# Example recursive function structure.
# Replace the base condition with a real stopping condition when using recursion.
def function():
    # No operation here; this is only a structural example.
    return


# reverse order

def func(num):
    if num == 0:
        return
    print(num, end=' ')  # Expected output: 5 4 3 2 1
    func(num - 1)

func(5)
print()


# inorder order

def func(num):
    if num == 0:
        return
    func(num - 1)
    print(num, end=' ')  # Expected output: 1 2 3 4 5

func(5)
print()


# addition

def sumofdigits(n):
    if n == 0:
        return 0
    return n + sumofdigits(n - 1)

print(sumofdigits(5))
# Expected output: 15


# product

def sumofdigits(n):
    if n == 0:
        return 1
    return n * sumofdigits(n - 1)

print(sumofdigits(5))
# Expected output: 120


# base, power

def power(base, pow):
    if pow == 0:
        return 1
    return base * power(base, pow - 1)

print(power(2, 3))
print(power(3, 3))
# Expected output:
# 8
# 27


def reverseofstr(s, ind):
    if ind == 0:
        return s[0]
    return s[ind] + reverseofstr(s, ind - 1)

l = "python"
print(reverseofstr(l, len(l) - 1))
# Expected output: nohtyp
















