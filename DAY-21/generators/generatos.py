# generators
# This file demonstrates generator usage in several ways
# without creating any additional helper functions.

# 1. Simple generator that yields numbers from 1 to 10.
def display():
    for i in range(1, 11):
        yield i

n = display()
for i in range(10):
    print(next(n))
# Expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# 2. Generator that yields all factors of a number lazily.
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

n = factors(42)

try:
    while True:
        print(next(n))
except StopIteration:
    print("End of the program")
# Expected output:
# 1
# 2
# 3
# 6
# 7
# 14
# 21
# 42
# End of the program


# 3. A different factors function that returns a list of factors.
# This list is then converted into a generator using the wrapper below.
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def generators(res):
    for i in res:
        yield i

res = factors(60)
facts = generators(res)
for i in range(len(res)):
    print(next(facts))
# Expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 10
# 12
# 15
# 20
# 30
# 60


# 4. Build a list of prime numbers from 2 to 100 and then iterate
# the list using the same generators wrapper.
def primes():
    res = []
    for num in range(2, 101):
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                break
        else:
            res.append(num)
    return res

def generators(res):
    for i in res:
        yield i

res = primes()
g = generators(res)
for i in range(len(res)):
    print(next(g))
# Expected output: prime numbers from 2 to 100, each on its own line.