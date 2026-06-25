# syntax:
# var = lambda arguments: expression

add = lambda a, b: a + b
print(add(12, 13))  # Expected output: 25
print(add(22, 33))  # Expected output: 55

wish = lambda name: f'Welcome the python course {name}'
print(wish('rishi'))  # Expected output: Welcome the python course rishi
print(wish('varma'))  # Expected output: Welcome the python course varma

gst = lambda price: price + price * 0.18
print(gst(1000))  # Expected output: 1180.0
print(gst(600))   # Expected output: 708.0
print(gst(89000)) # Expected output: 105020.0

greatest = lambda a, b: a if a > b else b
print(greatest(18, 19))    # Expected output: 19
print(greatest(2000, 1900)) # Expected output: 2000
print(greatest(10, 30))    # Expected output: 30

iseven = lambda a: f"{a}-Even number" if a % 2 == 0 else f"{a}-odd number"
print(iseven(4))   # Expected output: 4-Even number
print(iseven(9))   # Expected output: 9-odd number
print(iseven(15))  # Expected output: 15-odd number

bill = lambda charge: charge if charge > 99 else charge + 30
print(bill(150))  # Expected output: 150
print(bill(45))   # Expected output: 75
print(bill(15))   # Expected output: 45

login = True
instock = True
status = lambda login, instock: ("You can buy product" if instock else "Product is out of stock") if login else "Login to buy a product"
print(status(login, instock))  # Expected output: You can buy product

l = [1, 2, 3, 4, 5, 6, 7]
res = list(map(lambda i: i**3, l))
print(res)  # Expected output: [1, 8, 27, 64, 125, 216, 343]

names = ['satya', 'rishi', 'varma']
t = list(map(lambda i: i.title(), names))
print(t)  # Expected output: ['Satya', 'Rishi', 'Varma']

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = list(filter(lambda i: i % 2 == 0, l))
print(res)  # Expected output: [2, 4, 6, 8, 10, 12]

l = [1, 2, 3, 4, 5, 6, 7]
res = list(filter(lambda i: i > 5, l))
print(res)  # Expected output: [6, 7]

l = [1, 2, 3, 4, 5, 6, 7]
res = list(filter(lambda i: i % 3 == 0, l))
print(res)  # Expected output: [3, 6]

from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
s = reduce(lambda sum, i: sum + i, l)
p = reduce(lambda pro, i: pro * i, l)
m = reduce(lambda max, i: max if max > i else i, l)
print(s, p, m)  # Expected output: 78 479001600 12

# Sorting dictionary items with lambda as sort key

d = {'subbu': 50, 'nagendra': 40, 'naresh': 60, 'dinesh': 80, 'sahith': 70}
print(dict(sorted(d.items())))  # Expected output: {'dinesh': 80, 'nagendra': 40, 'naresh': 60, 'sahith': 70, 'subbu': 50}
print(dict(sorted(d.items(), key=lambda i: i[1])))  # Expected output: {'nagendra': 40, 'subbu': 50, 'naresh': 60, 'sahith': 70, 'dinesh': 80}
print(dict(sorted(d.items(), reverse=True)))  # Expected output: {'sahith': 70, 'naresh': 60, 'nagendra': 40, 'dinesh': 80, 'subbu': 50}
print(dict(sorted(d.items(), key=lambda i: i[1], reverse=True)))  # Expected output: {'dinesh': 80, 'sahith': 70, 'naresh': 60, 'subbu': 50, 'nagendra': 40}


