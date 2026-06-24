# Program to check if a number is even or odd

# Input: Take an integer from the user
num = int(input("Enter a number: "))

# Check if the number is even (divisible by 2 with remainder 0)
if num % 2 == 0:
    print("Even number")
else:
    # Otherwise, the number is odd
    print("Odd number")