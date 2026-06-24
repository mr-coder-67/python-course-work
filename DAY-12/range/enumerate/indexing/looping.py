
# Demonstrate `enumerate()` on a string: returns (index, character)
s = 'looping'
for i in enumerate(s):
    # i is a tuple like (index, value); print index and value
    print(i[0], i[1])


# Enumerate over a list of integers and print index and element
l = [1, 2, 3, 5, 6, 7]
for i in enumerate(l):
    print(i[0], i[1])


# Another list example (same structure)
t = [1, 2, 3, 5, 6, 7]
for i in enumerate(t):
    print(i[0], i[1])


# You can reuse variable names; this demonstrates enumerate again
s = [1, 2, 3, 5, 6, 7]
for i in enumerate(s):
    print(i[0], i[1])
    
