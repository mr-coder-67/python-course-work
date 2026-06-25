
d = {'sugar' : 40, 'salt' : 20, 'cooking oil' : 80, 'chilli': 60}

res = dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1 = dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))

print(res)
print(res1)
# Expected output:
# {'sugar': 47.2, 'salt': 23.6, 'cooking oil': 94.4, 'chilli': 70.8}
# {'sugar': 20.0, 'salt': 10.0, 'cooking oil': 40.0, 'chilli': 30.0}

#filter
d = {'sugar' : 40, 'salt' : 20, 'cooking oil' : 80, 'chilli': 60}

res = dict(filter(lambda i:i[1]>50,d.items()))
res1 = dict(filter(lambda i:i[1]<50,d.items()))

print(res,res1)
# Expected output: ({'cooking oil': 80, 'chilli': 60}, {'sugar': 40, 'salt': 20})

res1 = []
for i in range(1,11):
    res1.append(i)

res2 = [i for i in range(1,11)]

print(res1)
print(res2)
# Expected output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res3 = []
for i in range(3,31,3):
    res3.append(i)

res4 = [i for i in range(3,31,3)]

print(res3)
print(res4)
# Expected output:
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

res5 = []
for i in range(2,51,2):
    res5.append(i)

res6 = [i for i in range(2,51,2)]
print(res5)
print(res6)
# Expected output:
# [2, 4, 6, ..., 50]
# [2, 4, 6, ..., 50]

#simple if
a = 'python programming'
l =[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)

print(l)

l1 = [i for i in a if i in 'aeiouAEIOU' ]
print(l1)
# Expected output:
# ['o', 'o', 'a', 'i']
# ['o', 'o', 'a', 'i']

# list comprehension templates (examples):
# l = [val for var in seq]
# l = [val for var in seq if condition]
# l = [val if condition else other_val for var in seq]

a = [1,2,3,4,5,6,7,22,42]
l = []
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)

print(l)

l1 = [i if i%2==0 else 0 for i in a]
print(l1)
# Expected output:
# [0, 2, 0, 4, 0, 6, 0, 22, 42]
# [0, 2, 0, 4, 0, 6, 0, 22, 42]

# taking input into list (interactive)
# l = [int(input(f"Enter the number - {i+1}:")) for i in range(10)]
# print(l)

l = []
for i in range(3):
    for j in range (1,4):
        l.append(j)
print(l)

l1 = [j for i in range (3) for j in range(1,4)]
print(l1)
# Expected output:
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

l = [[j for j in range(1,4)] for i in range (3)]

print(l)
# Expected output:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

s = set()
for i in range(1,11):
    s.add(i)

s1 = {i for i in range(1,11)}

print(s,s1)
# Expected output: {1,2,...,10} {1,2,...,10}

d = {}
for i in range(1,11):
    d[i] = i*i

print(d)

res = {i:i*i for i in range(1,11)}
print(res)
# Expected output: {1:1, 2:4, ..., 10:100}

# interactive dict comprehension example (commented out to avoid blocking execution):
# res = {input("Enter the name: "):int(input("Enter the mark: ")) for i in range (5)}
# print(res)

# Generators
def display():
    # yield each block label from the list
    l = ['1..50', '51..100', '101..150', '151..200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]

scroll = display()  # create generator object

print(next(scroll))  # Expected output: 1..50
print(next(scroll))  # Expected output: 51..100
print(next(scroll))  # Expected output: 101..150
print(next(scroll))  # Expected output: 151..200