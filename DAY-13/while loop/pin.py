pin = 1234
for i in range(5):
    e_pin=int(input("enter the pin :"))
    if e_pin==pin:
        print("Unlock the phone")
        break
    else:
        print("Incorrect password")
else:
    print("Try again, after 60 Second")
    
