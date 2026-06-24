# Examples demonstrating Python 'for' loop syntax

# 1) Iterate over a list
sequence = [10, 20, 30, 40]
for var in sequence:
    # 'var' takes each element from the list in order
    print(var)


# 2) Iterate using range() to get indices/numbers
for i in range(5):
    # prints 0,1,2,3,4
    print(i)


# 3) Iterate over a string (character by character)
text = 'hello'
for ch in text:
    print(ch)


# 4) Iterate over dictionary items (key and value)
data = {'a': 1, 'b': 2, 'c': 3}
for key, value in data.items():
    print(f"{key}: {value}")