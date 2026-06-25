
# generator example 1: yield fixed ranges from a list

def display():
    l = ['1..50', '51..100', '101..200', '201..250']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]

scroll = display()
print(next(scroll))  # expected output: 1..50
print(next(scroll))  # expected output: 51..100
print(next(scroll))  # expected output: 101..200
print(next(scroll))  # expected output: 201..250

# generator example 2: yield numbers from 1 to 10

def display():
    for i in range(1, 11):
        yield i

n = display()
for i in range(10):
    print(next(n))  # expected output: numbers 1 through 10 each on its own line

# factors using a generator function

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

n = factors(56)
try:
    while True:
        print(next(n))  # expected output: 1 2 4 7 8 14 28 56
except StopIteration:
    print("End of the program")  # expected output after factors: End of the program

# another method: build a list of factors then yield them one by one

def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def generatos(res):
    for i in res:
        yield i

res = factors(60)  # expected list: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
facts = generatos(res)
for i in range(len(res)):
    print(next(facts))  # expected output: factors of 60 printed one per line

# primes from 2 to 100, then yield them from a generator

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

res = primes()  # expected output list starts with [2, 3, 5, 7, 11, ...]
g = generators(res)
for i in range(len(res)):
    print(next(g))  # expected output: all prime numbers from 2 to 100 printed one per line
                
