# stored credentials (username, password)
data = ('abc', '1234')

# Prompt the user to enter username and password separated by space
try:
    username, password = input("Enter the username and password (separated by space): ").split()
except ValueError:
    # If the user doesn't provide exactly two values, inform and exit
    print("Please enter both username and password separated by a space.")
else:
    # remove accidental surrounding whitespace
    username = username.strip()
    password = password.strip()

    # compare input credentials to stored credentials
    if data == (username, password):
        print("Login successful")
    else:
        print("Invalid login")