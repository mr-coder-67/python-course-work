password=input("Enter the password: ")
if len(password)>8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
        
    if len(s)==4:
        print("Strong password")
    else:
        print("weak password")
        
else:
    print("Weak Strong")
        