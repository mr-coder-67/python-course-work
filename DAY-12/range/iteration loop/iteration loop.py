# Examples of iteration (loops) in Python with comments

# 1) Iterate over a string and print vowels
s = 'looping statement'
vowels = 'aeiouAEIOU'
for ch in s:
    # Check if the current character is a vowel
    if ch in vowels:
        print(ch)


# 2) Iterate over a list and print even numbers
l = [24, 26, 32, 73, 76, 86, 85, 7, 92, 54, 66]
for num in l:
    # If number is divisible by 2, it is even
    if num % 2 == 0:
        print(num)


# 3) Iterate over a dictionary and print keys that have a truthy value
d = {'laptop': 0, 'charger': 2, 'keyword': 10, 'phone': 15, 'tab': 0}
for key, val in d.items():
    # Only print keys where the value is truthy (non-zero)
    if val:
        print(key)


# 4) Iterate over a tuple using index and multiply index by the value
t = (9, 2, 13, 4, 5, 6)
for i in range(len(t)):
    # Multiply index by the element at that index
    print(i * t[i])


# 5) Iterate over a set of names and print each name in uppercase
names = {'subbu', 'ashrutha', 'dinesh', 'panda'}
for name in names:
    # Use upper() with no arguments to convert to uppercase
    print(name.upper())