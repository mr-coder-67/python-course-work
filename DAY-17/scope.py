# local scope
# The variable n inside display() exists only within the function.
def display():
    n = 10
    print("Inside:", n)

display()
# The following line would fail because n is not defined outside the function.
# print("outside:", n)


# global scope
n = 10

def display():
    # This function reads the global n value.
    print("Inside:", n)

display()
print("outside:", n)
# Expected output:
# Inside: 10
# outside: 10


def display():
    global n
    # This assignment changes the global n variable.
    n = 10
    print("Inside:", n)

display()
print("outside:", n)
# Expected output:
# Inside: 10
# outside: 10


def display(n):
    # This n is a local parameter, separate from the global n.
    n += 10
    print("Inside:", n)

n = 10
display(n)
print("outside:", n)
# Expected output:
# Inside: 20
# outside: 10


# global modification with global keyword

def display():
    global n
    n += 10
    print("Inside:", n)

n = 10
display()
print("outside:", n)
# Expected output:
# Inside: 20
# outside: 20


def outer():
    n = 10
    def inner(n):
        n += 10
        print("Inner Function:", n)
    inner(n)

    print("Outer Function:", n)

outer()
# Expected output:
# Inner Function: 20
# Outer Function: 10


def outer():
    n = 10
    def inner():
        nonlocal n
        n += 10
        print("Inner Function:", n)
    inner()

    print("Outer Function:", n)

outer()
# Expected output:
# Inner Function: 20
# Outer Function: 20


# do not overwrite built-in names
s = 'python'
print(len(s))
# Expected output: 6

len = 5
print(len)
# Expected output: 5
# The following line would fail because len is now an int, not the built-in function:
# print(len(s))



