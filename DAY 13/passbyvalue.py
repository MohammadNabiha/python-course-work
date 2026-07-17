#global keyword
'''def display():
    global num
    num+=10
    print("Inside num:",num)
num=10
display()
print("outside num:",num)'''
#pass by value-int
'''def display(num):
    num+=10
    print("Inside num:",num)
num=10
display(num)
print("Outer num:",num)'''
#pass by value-float
'''def display(num):
    num+=10
    print("Inside num:",num)
num=10.5
display(num)
print("Outer num:",num)'''
#pass by value-boolean
'''def display(num):
    num=False
    print("Inside num:",num)
num=True
display(num)
print("Outer num:",num)'''
#pass by value-string
'''def display(num):
    num=num+"Programming"
    print("Inside num:",num)
num="python"
display(num)
print("Outer num:",num)'''
#function inside the function,want the change outside the function too then we use nonlocal keyword
'''def courses():
    course="Java"
    print("In the start:",course)
    def change():
        nonlocal course
        course="Python"
        print("Changed:",course)
    change()
    print("Final:",courses)
courses()'''
#Recursion:1 to 10
'''def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)'''
#recursion 10 to 1
'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)'''
#recursion :python
'''def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s='Python'
display(s,0)'''
#recursion--nohtyp
'''def display(s,ind):
    if ind==len(s):
        return
    display(s,ind+1)
    print(s[ind])
s='Python'
display(s,0)'''
#recursion--p py pyt pyth......
'''def display(s,ind):
    if ind==len(s)+1:
        return
    print(s[:ind])
    display(s,ind+1)
s="python Programing"
display(s,1)
'''
#recursion -
'''def display(s,ind):
    if ind==len(s)+1:
        return
    display(s,ind+1)
    print(s[:ind])
s="python Programing"
display(s,1)'''
#recursion
'''def display(s,ind,width):
    if ind==len(s)-width+1:
        return
    print(s[ind:ind+width:])
    display(s,ind+1,width)
    
s="python Programing"
display(s,0,4)'''
'''def display(n,s):
    n=n%10
    s+=n
    n//10
    display(n,s)
    print(s)
display(123,0)'''



    
    


