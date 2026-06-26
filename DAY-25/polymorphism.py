# #polymorphism = same function , but diff action
# # it has 2 methods- method overriding and method overloading
# #method overriding   = same method name in parent and child class
# #method overloading = same method name but diff args in same class
# #python does not support method overloading, but we can achieve it using default arguments or variable-length arguments.



# ###method overriding example

# class Hotstar:
    
#     def __init__(self, name):
#         self.name = name
#         print(f'hi {self.name}, welcome to the Hotstar')
    
     
#     def login(self):
#          print("you can login" )
#     def dashboard(self):
#         print("you can see dashboard")
#     def search(self):
#         print("you can search movies / shows")
#     def language(self):
#         print("you can select language")
#     def playcontrollers(self):
#         print("you can use play and play the video")
        
    
#     def ads(self):
#         print("ads will run ")
#     def movies(self):
#         print("you can watch limited movies")
#     def sports(self):
#         print("limited time you can watch sports")
#     def quality(self):
#         print("you can watch in limited quality")
    
# #calling objetcs in hotstar
# akhil = Hotstar('Akhil')
# akhil.login()
# akhil.dashboard()
# akhil.search()
# akhil.language()
# akhil.playcontrollers()
# akhil.ads()
# akhil.movies()
# akhil.sports()
# akhil.quality()

# #for premium hotstar users

# class PremiumHotstar(Hotstar):
#     def __init__(self, name):
#         self.name = name
#         # super().__init__(name)
#         print(f'hi {self.name}, welcome to the Premium Hotstar')
    
#     def ads(self):
#         print("ads will not run ")
#     def movies(self):
#         print("you can watch unlimited movies")
#     def sports(self):
#         print("unlimited time you can watch sports")
#     def quality(self):
#         print("you can watch in high quality")

# #calling objects in premium hotstar
# Naresh=PremiumHotstar('Naresh')
# Naresh.login()
# Naresh.dashboard()
# Naresh.search()
# Naresh.language()
# Naresh.playcontrollers()
# Naresh.ads()
# Naresh.movies()
# Naresh.sports()
# Naresh.quality()


# ### method overloading example

class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __eq__(self, other):
        return self.n == other.n
    def __lt__(self, other):
        return self.n < other.n
    def __gt__(self, other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)
    
    
#calling objects in number class
n1 = Number(10)
n2 = Number(5)

print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)
print("Division:", n1 / n2)

print("Equal:", n1 == n2)
print("Less than:", n1 < n2)
print("Greater than:", n1 > n2)
print("String representation:", n1,n2)
print("String representation:", n1)
print("String representation:", n2)
print("String representation:", str(n1))
print("String representation:", str(n2))

