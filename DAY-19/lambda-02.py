#Lamda Functions


#Lamda Functions


# addition using lambda
add = lambda a, b: a + b
print(add(12, 13))  # Expected output: 25
print(add(23, 76))  # Expected output: 99



# print names using lambda
wish = lambda name: f'welcome the python course {name}'
print(wish('subbu'))   # Expected output: welcome the python course subbu
print(wish('Naresh'))  # Expected output: welcome the python course Naresh




# calc GST
gst = lambda price: price + price * 0.18
print(gst(1000))      # Expected output: 1180.0
print(gst(29000))     # Expected output: 34220.0



# less than or Greater
greatest = lambda a, b: a if a > b else b
print(greatest(10, 3))   # Expected output: 10
print(greatest(9, 22))   # Expected output: 22
print(greatest(4, 4))    # Expected output: 4



# Even or Odd
iseven = lambda a: f'{a}--Even Number' if a % 2 == 0 else f'{a}--Odd Number'
print(iseven(9))    # Expected output: 9--Odd Number
print(iseven(10))   # Expected output: 10--Even Number
print(iseven(124))  # Expected output: 124--Even Number



# Billing example with conditional lambda
bill = lambda charge: charge if charge > 99 else charge + 30
print(bill(990))  # Expected output: 990
print(bill(90))   # Expected output: 120
print(bill(190))  # Expected output: 190
print(bill(100))  # Expected output: 100
print(bill(99))   # Expected output: 129



# Login and stock status
login = False
instock = False

status = lambda login, instock: ("you can buy product" if instock else "product is out of stock") if login else "login to buy a product"
print(status(login, instock))  # Expected output when login=False, instock=False: login to buy a product



## --- MAP examples --- ##
# List: cube each element
l = [1, 2, 3, 4, 5, 6, 7]
res = list(map(lambda i: i ** 3, l))
print(res)  # Expected output: [1, 8, 27, 64, 125, 216, 343]



# Title-case names
names = ['Naresh', 'akhil', 'ajay']
t = list(map(lambda i: i.title(), names))
print(t)  # Expected output: ['Naresh', 'Akhil', 'Ajay']



# --- FILTER examples ---
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = list(filter(lambda i: i % 2 == 0, l))
print(res)  # Expected output: [2, 4, 6, 8, 10, 12]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = list(filter(lambda i: i > 5, l))
print(res)  # Expected output: [6, 7, 8, 9, 10, 11, 12]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = list(filter(lambda i: i % 3 == 0, l))
print(res)  # Expected output: [3, 6, 9, 12]




from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = reduce(lambda sum, i: sum + i, l)
p = reduce(lambda pro, i: pro * i, l)
print(s, p)  # Expected output: 45 362880



from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = reduce(lambda sum, i: sum + i, l)
p = reduce(lambda pro, i: pro * i, l)
m = reduce(lambda max, i: max if max > i else i, l)
mi = reduce(lambda minv, i: minv if minv < i else i, l)

print(s, p, m, mi)  # Expected output: 45 362880 9 1



d = {'subbu': 50, 'nagendra': 40, 'naresh': 60, 'dinesh': 80, 'sahith': 70}
print(dict(sorted(d.items())))  # Expected output: keys sorted ascending
print(dict(sorted(d.items(), key=lambda i: i[1])))  # Expected output: values sorted ascending
print(dict(sorted(d.items(), reverse=True)))  # Expected output: keys sorted descending
print(dict(sorted(d.items(), key=lambda i: i[1], reverse=True)))  # Expected output: values sorted descending



d = {'sugar': 40, 'salt': 20, 'cooking oil': 80, 'chilli': 60}
res = dict(map(lambda i: (i[0], i[1] + i[1] * 0.18), d.items()))
res1 = dict(map(lambda i: (i[0], i[1] - i[1] * 0.5), d.items()))
print(res)   # Expected: prices increased by 18%
print(res1)  # Expected: prices decreased by 50%



d = {'sugar': 40, 'salt': 20, 'cooking oil': 80, 'chilli': 60}
res = dict(filter(lambda i: i[1] > 50, d.items()))
res1 = dict(filter(lambda i: i[1] < 50, d.items()))
print(res, res1)  # Expected output: ({'cooking oil': 80, 'chilli': 60}, {'sugar': 40, 'salt': 20})






d={'subbu':50,'nagendra':40,'naresh':60,'dinesh':80,'sahith':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))





d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)






d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))
print(res,res1)



