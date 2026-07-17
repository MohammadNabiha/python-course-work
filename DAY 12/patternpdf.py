#                       BASIC PATTERNS
#Square Pattern
'''n=int(input("Enter a number:"))
for i in range(n):
    for j in range (n):
        print("*",end=" ")
    print()'''
#Rectangle Pattern (5x3)
'''n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
for i in range(m):
    for j in range (n):
        print("*",end=" ")
    print()'''
#3. Right-Angled Triangle
'''n=int(input("enter size:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#Inverted Right Triangle
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
'''
#5. Same Number Triangle
'''n=int(input("enter size:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()'''
#Increasing Numbers per Row
'''n=int(input("enter size:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
#Continuous Numbers Triangle
'''n=int(input("Enter a number:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()'''
#Alphabet Triangle
'''n=int(input("enter size:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()'''
#Single Column
'''n=int(input("enter a number;"))
for i in range(n):
    print("*")'''
#single Row
'''n=int(input("Enter a number:"))
for i in range(n):
            print("*",end=" ")'''
    
#                            Intermediate Patterns
#Pyramid
'''n=int(input("Enter a size:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for t in range(2*i+1):
        print("*",end=" ")
    print()'''
#Inverted Pyramid
'''n=int(input("Enter a size:"))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for t in range(2*(n-i)-1):
        print("*",end=" ")
    print()'''
#Diamond
rows = int(input("Enter number of rows: "))

# Upper part
for i in range(1, rows + 1):

    # Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Lower part
for i in range(rows - 1, 0, -1):

    # Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()
    
        

