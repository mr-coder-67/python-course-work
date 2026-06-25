# int float complex str tuple set dict bool
# int float complex str tuple bool -> immutable passing
# list set dict -> mutable


# int

def update(n):
    # Integers are immutable, so a new value is created inside the function.
    n += 10
    print("Inside:", n)

n = 10
update(n)
print("outside:", n)

# Expected output:
# Inside: 20
# outside: 10


# float

def update(n):
    # Floats are immutable; the original value stays unchanged outside.
    n += 10
    print("Inside:", n)

n = 10.4
update(n)
print("outside:", n)

# Expected output:
# Inside: 20.4
# outside: 10.4

# complex

def update(n):
    # Complex numbers are immutable, so the outside value remains unchanged.
    n += 10
    print("Inside:", n)

n = 3 + 4j
update(n)
print("outside:", n)

# Expected output:
# Inside: (13+4j)
# outside: (3+4j)


# string

def update(n):
    # Strings are immutable; concatenation creates a new string inside the function.
    n += ' python'
    print("Inside:", n)

n = ' lang'
update(n)
print("outside:", n)

# Expected output:
# Inside:  lang python
# outside:  lang

# list

def update(n):
    # Lists are mutable, so append modifies the same object.
    n.append(6)
    print("Inside:", n)

n = [1, 2, 3, 4, 5]
update(n)
print("outside:", n)

# Expected output:
# Inside: [1, 2, 3, 4, 5, 6]
# outside: [1, 2, 3, 4, 5, 6]


# tuple

def update(n):
    # Tuples are immutable, so n += (6,) creates a new tuple inside the function.
    n += (6,)
    print("Inside:", n)

n = (1, 2, 3, 4, 5)
update(n)
print("outside:", n)

# Expected output:
# Inside: (1, 2, 3, 4, 5, 6)
# outside: (1, 2, 3, 4, 5)


# set

def update(n):
    # Sets are mutable, so add modifies the same object.
    n.add(6)
    print("Inside:", n)

n = {1, 2, 3, 4, 5}
update(n)
print("outside:", n)

# Expected output:
# Inside: {1, 2, 3, 4, 5, 6}
# outside: {1, 2, 3, 4, 5, 6}


# dict

def update(n):
    # Dictionaries are mutable, so assigning a new key updates the original object.
    n[6] = 6
    print("Inside:", n)

n = {2: 2, 3: 3, 5: 2}
update(n)
print("outside:", n)

# Expected output:
# Inside: {2: 2, 3: 3, 5: 2, 6: 6}
# outside: {2: 2, 3: 3, 5: 2, 6: 6}

# bool

def update(n):
    # Booleans are immutable; True behaves like 1 when added.
    n += True
    print("Inside:", n)

n = False
update(n)
print("outside:", n)

# Expected output:
# Inside: 1
# outside: False








