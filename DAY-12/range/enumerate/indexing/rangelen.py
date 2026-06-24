
# Demonstrate iterating over a string using index positions
# `range(len(s))` produces indices 0..len(s)-1, allowing access to characters by index
s = 'looping Statement'
for i in range(len(s)):
    # print index and the character at that index
    print(i, s[i])


# Demonstrate iterating over a list using indices
l = [7, 2, 3, 4, 6, 1, 5]
for i in range(len(l)):
    # print index and the list element at that index
    print(i, l[i])


# Another example with the same list (named `t` here)
# Using index-based iteration is useful when you need the index and value
t = [7, 2, 3, 4, 6, 1, 5]
for i in range(len(t)):
    print(i, t[i])

