import logic as lg

# Start ATM program by asking the user to log in.
# The login function should return True when authentication succeeds.
if lg.login():
    print("=========Welcome to the ATM=========")
    # Loop until the user chooses to exit.
    while True:
        lg.menu()  # Show the available ATM options.
        ch = input("Enter the choice: ").lower()

        if ch == 'c':
            # Check current account balance.
            lg.checkBalance()
        elif ch == 'd':
            # Deposit money into the account.
            lg.deposit()
        elif ch == 'w':
            # Withdraw money from the account.
            lg.withdraw()
        elif ch == 'v':
            # View past transaction records.
            lg.viewTransactions()
        elif ch == 'e':
            # Exit the ATM program.
            print("Thankyou")
            break