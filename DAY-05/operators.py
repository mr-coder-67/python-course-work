# String operator examples in Python

# Assign string values to variables
s = 'python programming lang'
print('Initial string:', s)
print('Type of s:', type(s))

# Empty string assignment
s = ''
print('\nEmpty string:', repr(s))
print('Type of empty string:', type(s))

# String concatenation with +
a = 'codegnan'
b = 'psf'
print('\nConcatenation result:', a + b)

# Reset variables and show concatenation again
a = 'codegnan'
b = 'psf'
print('Concatenation with original values:', a + b)

# String repetition with *
print('\nRepeat string 3 times:', a * 3)
print('Repeat string with a space 4 times:', 'python ' * 4)

# Additional string examples
message = 'hello'
print('\nMessage:', message)
print('First character:', message[0])
print('Substring from index 1 to 4:', message[1:4])
print('Uppercase:', message.upper())
print('Contains "p"?', 'p' in message)
print('Does not contain "z"?', 'z' not in message)
