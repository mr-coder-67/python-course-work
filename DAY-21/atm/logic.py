# Sample ATM data stored in memory.
# Each account number maps to PIN, balance and a transaction history list.
data = {
    123456: {'pin': 1234, 'balance': 5000, 'history': []},
    234561: {'pin': 1234, 'balance': 8000, 'history': []},
    345612: {'pin': 1234, 'balance': 7000, 'history': []},
    456123: {'pin': 1234, 'balance': 4000, 'history': []}
}


def login():
    # Ask the user for account number and PIN, then verify login.
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin number: "))

    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False


def menu():
    # Display the ATM menu choices to the user.
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')


def checkBalance():
    # Show the current balance for the logged-in account.
    print("Current Balance:", data[acc_num]['balance'])


def deposit():
    # Take a deposit amount, add it to the balance, and record the transaction.
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['history'].append(f'{amount} - Deposit +++++++')
    print("Deposit Successful")


def withdraw():
    # Withdraw money only if the account has enough balance.
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['history'].append(f'{amount} - Withdraw --------')
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")


def viewTransactions():
    # Print the list of past transaction records for the account.
    if data[acc_num]['history']:
        print('-------Transactions----------')
        for i in data[acc_num]['history']:
            print(i)
        print('-------End----------')
    else:
        print("No Transaction History")