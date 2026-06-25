# Encapsulation example: restricting direct access to internal data
# Encapsulation means hiding internal object details and providing methods to access them.
# Public attributes like username can be changed directly.
# Private attributes use name mangling (double underscore) to prevent direct access.

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private attribute, should not be changed directly
        self.followers = []         # public attribute

    def getpassword(self):
        # getter method returns the private password value.
        return self.__password

    def setpassword(self, newpassword):
        # setter method updates the private password value.
        self.__password = newpassword
        print(f'welcome to the Instagram, {self.username}')
        # expected output when password changes: welcome to the Instagram, vamsi

vamsi = Instagram('vamsi', 'vamsi@123')

print("Before username:", vamsi.username)
# expected output: Before username: vamsi
vamsi.username = 'Akhil'
print("After username:", vamsi.username)
# expected output: After username: Akhil

print("Before password :", vamsi.getpassword())
# expected output: Before password : vamsi@123
vamsi.setpassword('Akhil@123')
# expected output: welcome to the Instagram, Akhil
print("After password:", vamsi.getpassword())
# expected output: After password: Akhil@123