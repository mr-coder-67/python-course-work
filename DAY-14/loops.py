n=int(input("enter the size:"))
#for row in range (n):
#    for col in range(n):
 #       print('*',end=' ' )
            #rint()

#for row in range (n):
 #   for col in range(row+1):
  #      print('*', end= '')
   # print()

#   for i in range (n):
   # for i in range (n-i):
   #     print('*', end ='')
    #print()

#for i in range(n):
  #  for sp in range (n-1-i):
   #     print('',end='')
   # for j in range(i+1):
    #    print('*', end='')
   # print()
for row in range (n):
    for sp in range (row):
        print('',end='')
    for col in range(n-row):
        print('*', end='')
    print()
    
    
    
