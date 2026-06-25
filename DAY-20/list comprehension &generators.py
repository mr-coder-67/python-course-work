# List Comprehensions and Generators
#
# List Comprehension - definition:
# A concise way to create lists using a single expression. It combines an
# expression and a for-loop, optionally with an if-condition, into one line.
# Syntax examples:
#   [expr for item in iterable]
#   [expr for item in iterable if condition]
# Benefits: more readable and often faster than building lists with loops.
#
# Generators - definition:
# A generator is an iterator defined with a function that uses `yield` to
# produce items one at a time, pausing its state between yields. Generators
# are memory-efficient for large sequences because they produce items lazily.
# Syntax example:
#   def gen():
#       yield value
# Use-case: streaming data, large computations, or pipelines where you don't
# need the whole list in memory.
#
# Examples for both concepts follow below.

res = []
for i in range(1, 11):
    res.append(i)
print(res)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res3 = []
for i in range(3, 31, 3):
    res3.append(i)
print(res3)  # Expected output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

res4 = [i for i in range(2, 51, 2)]
print(res4)  # Expected output: [2, 4, 6, ..., 50]


#

# List comprehensions examples with expected outputs

res = []
for i in range(1, 11):
    res.append(i)
print(res)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


res3 = []
for i in range(3, 31, 3):
    res3.append(i)
print(res3)  # Expected output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


res = [i for i in range(5, 51, 10)]
print(res)  # Expected output: [5, 15, 25, 35, 45]


# String: extract vowels
a = "Python Programming"
l = []
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)  # Expected output: ['o', 'o', 'a', 'i']

# Using comprehension
l1 = [i for i in a if i in 'aeiouAEIOU']
print(l1)  # Expected output: ['o', 'o', 'a', 'i']


# list comprehension templates (examples):
# l = [val for var in seq]
# l = [val for var in seq if condition]
# l = [val if condition else other_val for var in seq]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 5, 87, 56, 45, 98]
l = []
for i in a:
    if i % 2 == 0:
        l.append(i)
    else:
        l.append(0)
print(l)  # Expected output: [0, 2, 0, 4, 0, 6, 0, 8, 0, 12, 0, 0, 56, 0, 98]

# comprehension equivalent
l1 = [i if i % 2 == 0 else 0 for i in a]
print(l1)  # Expected output: same as above


# interactive input example (commented out to avoid blocking execution)
# l = [int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
# print(l)


# nested loops -> flat list
l = []
for i in range(3):
    for j in range(1, 4):
        l.append(j)
print(l)  # Expected output: [1,2,3,1,2,3,1,2,3]

# comprehension form
l1 = [j for i in range(3) for j in range(1, 4)]
print(l1)  # Expected output: same as above


# nested comprehension producing a 2D list
l1 = [[j for j in range(1, 4)] for i in range(3)]
print(l1)  # Expected output: [[1,2,3],[1,2,3],[1,2,3]]


# set comprehension
s = set()
for i in range(1, 11):
    s.add(i)
print(s)

s1 = {i for i in range(1, 11)}
print(s1)  # Expected output: {1,2,...,10}



## Dict comprehensions
d = {}
for i in range(1, 11):
    d[i] = i * i
print(d)  # Expected output: {1:1, 2:4, ..., 10:100}


res = {i: i * i for i in range(1, 20)}
print(res)  # Expected output: squares from 1 to 19


# interactive dict comprehension (commented out):
# res = {input("Enter the name: "): int(input("Enter the Mark: ")) for i in range(5)}
# print(res)


## Generators
def display():
    l = ['1...50', '51...100', '101...150', '151...200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]

scroll = display()

print(next(scroll))  # Expected output: 1...50
print(next(scroll))  # Expected output: 51...100
print(next(scroll))  # Expected output: 101...150
print(next(scroll))  # Expected output: 151...200



