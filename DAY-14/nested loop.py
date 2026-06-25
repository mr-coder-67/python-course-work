# Example of nested loops in Python
# 1) Print every possible pair of characters from the string 'python'.

s = 'python'
for i in range(len(s)):
    for j in range(len(s)):
        # print character at position i followed by character at position j
        print(s[i], s[j], sep='', end=' ')

print()  # separate output sections with a newline

# 2) Calculate the sum of all elements in a 2D list using nested loops
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in l:
    for value in row:
        total += value
print(f'sum={total}')

# 3) Iterate through a dictionary of accounts and print details
accounts = {
    '1234': {'pin': '4557', 'balance': 2300},
    '5676': {'pin': '6782', 'balance': 9300},
    '7860': {'pin': '2346', 'balance': 5300},
    '3409': {'pin': '0977', 'balance': 8300}
}
for account_number in accounts:
    print('Account number:', account_number)
    print('pin number:', accounts[account_number]['pin'])
    print('balance:', accounts[account_number]['balance'])