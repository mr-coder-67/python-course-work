
# n=int(input())
# m=n//2
# for i in range(n):
#     if i<=m:
#         for j in range(i+1):
#             print('*',end='')
#     else:
#         for j in range(n-i):
#             print('*',end='')
#     print()


# #another method

# n=int(input())
# m=n//2
# for i in range(n):
#     if i<=m:
#         print('*'*(i+1),end='')
#     else:
#         print('*'*(n-i),end='')
#     print()


# n=int(input())
# m=n//2
# for i in range(n):
#     if i<=m:
#         print('  '*(m-i),end=' ')
#         print('* '*(i+1),end=' ')
#     else:
#         print('  '*(i-m),end=' ')
#         print('* '*(n-i),end=' ')
#     print()




n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()


# n=int(input())
# m=n//2
# for i in range(n):
#     if i<=m:
#         print(' '*(m-i)+'* '*(i+1),end=' ')
#     else:
#         print(' '*(i-m)+'* '*(n-i),end=' ')
#     print()





# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j == n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()



# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()





# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or j==i or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()



# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==m or j==0 or j == n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()


# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==m or j==0 or j == n-1 or i == n-1    :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()


# n=int(input())

# for i in range(n):
#     for j in range(n):
#         if i==0  or j==0 or i == n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()


# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0  or j==0 or i == m:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()

# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0  or j==0 or i == m or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()


# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if j==0  or  i == m or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()

# n=int(input())
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0  or  j == m or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()

# n=int(input('Enter pattern size: '))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0  or  j == m or j>=m or i>=m :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()