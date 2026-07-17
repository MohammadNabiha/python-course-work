'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print("*",end=' ')
    print()'''
'''n=int(input("Enter a number:"))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()'''
'''n=int(input("enter a number:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()'''
'''n=int(input("Enter a number:"))
for i in range(n):
    for s in range(n-i-1):
        print(' ',end=' ')
    for c in range(i+1):
        print('*',end=' ')
    print()'''
'''n=int(input("Enter a number:"))
for i in range(n):
    for s in range(i):
        print(' ',end=' ')
    for c in range(n-i):
        print('*',end=' ')
    print()'''
'''n=int(input("Enter a number:"))
for i in range(n):
    for s in range(n):
        if s%2==0:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()'''
#or
'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(int(col%2==0),end=' ')
    print()'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(int(not(col%2==0)),end=' ')
    print()
'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(int((row+col)%2==0),end=' ')
    print( )'''
'''n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(int(not(row+col)%2==0),end=' ')
    print( )'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i%2==0 or j%2==0:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or n//2==i or n//2==j :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==4 or i==j :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n-1 and j<=n//2) or (i>=n//2 and j==n//2)or (i==n//2and j>=n//2) or (j==n-1and i==n//2)  :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()


