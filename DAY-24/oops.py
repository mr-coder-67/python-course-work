# OOP example using a class, instance, class method, and static method.
# class -> a blueprint for creating objects.
# attribute -> a variable stored inside a class or instance.
# method -> a function defined inside a class.
# object -> an instance created from a class.

class Flipkart:
    discount = 10
    product = ['laptop', 'phone', 'mouse', 'charger']

    @classmethod
    def showproduct(cls):
        # classmethod receives the class itself as the first argument.
        # It is used to access class-level attributes like product.
        print(cls.product)
        # expected output: ['laptop', 'phone', 'mouse', 'charger']

    def login(self, username, password):
        # instance method receives the instance as self.
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')
        # expected output: welcome to the flipkart akhil

    @staticmethod
    def banner():
        # staticmethod does not receive self or cls.
        # It can be called on the class or instance without accessing class data.
        print("10% discount is going on flipkart, shop now!")
        # expected output: 10% discount is going on flipkart, shop now!

akhil = Flipkart()
# create an instance of the Flipkart class.
akhil.login('akhil', 'akhil@123')
akhil.banner()
akhil.showproduct()