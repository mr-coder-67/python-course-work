# Generators — notes and examples
#
# Generators are iterators written like functions using `yield`.
# They produce values lazily (one at a time) and are memory-efficient
# for large sequences. Use generators when you don't need all values
# in memory at once.
#
# This file demonstrates simple generator usage, generators that yield
# factors of a number, converting a list to a generator (wrapper), and
# printing prime numbers using a generator-like wrapper.

# Simple generator: yields numbers 1..10 (one per `yield`).
def display():
    for i in range(1, 11):
        yield i

n = display()
for i in range(10):
    print(next(n))
# Expected output (each on its own line):
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


# Generator that yields factors of a given number (works lazily).
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
# Expected output for factors of 42 (each on new line):
# 1
# 2
# 3
# 6
# 7
# 14
# 21
# 42
# End of the program


# A variant: compute factor list (eager) and then create a simple
# generator wrapper that yields items from that list. This shows how
# you can turn any iterable into a generator-like sequence.
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def generators(res):
    for i in res:
        yield i

res = factors(60)
facts = generators(res)
for i in range(len(res)):
    print(next(facts))
# Expected output: factors of 60 printed one per line:
# 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60


# Prime numbers: build a list of primes (2..100) and then iterate
# through them using the same `generators` wrapper.
def primes():
    res = []
    for num in range(2, 101):
        # check divisibility up to num//2 (simple approach)
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
# Expected output (primes between 2 and 100, each on its own line):
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
# 53, 59, 61, 67, 71, 73, 79, 83, 89, 97