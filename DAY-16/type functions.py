
def display(name, email, pwd):
    # Positional arguments: values are passed in the same order as the parameters.
    print("Name:", name)
    print("Email:", email)
    print("password:", pwd)

# Expected output for positional calls:
# Name: akhil
# Email: shaikakhil281@gmail.com
# password: Akhi@_
# Name: Akhi@_
# Email: shaikakhil281@gmail.com
# password: akhil
# Name: shaikakhil@gmail.com
# Email: akhil
# password: Akhil@_

display('akhil', 'shaikakhil281@gmail.com', 'Akhi@_')
display('Akhi@_', 'shaikakhil281@gmail.com', 'akhil')
display('shaikakhil@gmail.com', 'akhil', 'Akhil@_')



def display(name, email, pwd):
    # Keyword arguments: values are passed by parameter name, so order can change.
    print("Name:", name)
    print("Email:", email)
    print("password:", pwd)

display(name='akhil', email='shaikakhil281@gmail.com', pwd='Akhi@_')
display(pwd='Akhi@_', email='shaikakhil281@gmail.com', name='akhil')
display(email='shaikakhil281@gmail.com', name='akhil', pwd='Akhil@_')



def display(name, email, pwd=''):
    # Default argument: pwd is optional and defaults to an empty string if not provided.
    print("Name:", name)
    print("Email:", email)
    print("password:", pwd)

# Expected output for default argument calls:
# Name: ashu
# Email: Ashrutha@gmail.com
# password: Ashu1@_
# Name: ashu
# Email: Ashrutha@gmail.com
# password:

display('ashu','Ashrutha@gmail.com','Ashu1@_')
# This call uses the default empty password for the second call.
display('ashu','Ashrutha@gmail.com')



def display(*names):
    # Variable positional arguments: collect all positional values into a tuple.
    print("Names:", names)
    

display('ashu', 'akhila', 'hansika', 'tejashwini')
display('komalatha', 'bhargavi')
display('akhila', 'supriya', 'dinesh')

# Expected output for variable positional arguments:
# Names: ('ashu', 'akhila', 'hansika', 'tejashwini')
# Names: ('komalatha', 'bhargavi')
# Names: ('akhila', 'supriya', 'dinesh')

def display(**names):
    # Variable keyword arguments: collects all named values into a dictionary.
    print("Names:", names)
    

display(k1='ashu', k2='akhila', k3='hansika', k4='tejashwini')
display(k1='komalatha', k2='bhargavi')









