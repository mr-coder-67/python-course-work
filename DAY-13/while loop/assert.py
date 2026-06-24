'''
status=True
assert status != None, "you need to update the Status"
print(status)

'''

# Declare values for name, age and batch
name = 'Akhil'
age = 22
batch = 55

# Assert is a debugging aid that checks a condition at runtime.
# If the condition is False, Python raises an AssertionError with the given message.
# Use assert when you want to catch programmer errors or invalid internal state,
# not for normal user input validation in production code.
assert (name != None and age != None and batch != None), "you need to update the Status"
print(name, age, batch)