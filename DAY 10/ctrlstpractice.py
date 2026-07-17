#Print Numbers from 1 to N (Using for loop)
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)'''
#Print Even Numbers from 1 to N (Using for loop)
'''n=int(input("Enter a number:"))
for i in range(2,n+1,2):
    print(i)
#Sum of Numbers from 1 to N (Using for loop)'''
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''
#Print Odd Numbers from 1 to N (Using for loop)
'''n=int(input("Enter a number:"))
for i in range(1,n+1,2):
    print(i)'''
#Find Factorial of a Number (Using for loop)
'''n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''
#Print Multiplication Table of N (Using for loop)
'''n=int(input("enter a number:"))
for i in range(1,11):
    print(f'{n}x{i}={n*i}')'''
#Check Prime Number (Using for loop)
'''n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("not prime")'''
#Sum of Digits of a Number (Using while loop)
'''n=int(input("Enter a number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n//=10
print(sum)'''
#Print Fibonacci Sequence up to N Terms (Using for loop)
'''n=int(input("Enter a number:"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c'''
#Count Numbers Divisible by 3 (Using for loop)
'''n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print(count)'''
#Check if a Number is Palindrome (Using while loop)
'''n=int(input("Enter a number:"))
original=n
reverse=0
while n>0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
if reverse==original:
    print("Palindrome")
else:
    print("not palindrome")'''
#Print Multiples of 5 up to N (Using for loop)
'''n=int(input("enter the number:"))
for i in range(5,n+1):
    if i%5==0:
        print(i)'''
#Find the Maximum of Three Numbers (Using for loop)
'''a,b,c=map(int,input("Enter three numbers:").split())
max_num=a
for i in [b,c]:
    if i>max_num:
        max_num=i
print("max_num:",max_num)'''
#Print Reverse of a Number
'''n=int(input("Enter a number:"))
reverse=0
while n>0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
print(reverse)'''
#Sum of First N Natural Numbers (Using for loop)
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''
#Print Numbers from N to 1 (Using while loop)
'''n=int(input("Enter a number:"))
while n>=1:
    print(i)
    i-=1'''
#Find Sum of Prime Numbers up to N
'''n=int(input("Enter a number:"))
sum=0
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        sum+=i
print(sum)'''
#Find the Product of Digits of a Number (Using while loop)
'''n=int(input("Enter a number:"))
m=1
while n>0:
    rem=n%10
    m=m*rem
    n=n//10
print(m)'''
#Print Numbers Divisible by Both 3 and 5 (Using for loop)
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)'''
#Find GCD of Two Numbers (Using while loop)
'''a=int(input("enter first number:"))
b=int(input("enter a second number:"))
if a>b:
    min=b
else:
    min=a
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print("HCF is:",hcf)'''
#Print Numbers Divisible by 7 (Using for loop)
'''n=int(input("enter a number:"))
for i in range(7,n+1,7):
    print(i,end=' ')'''
#Print Even Numbers in Reverse Order (Using while loop)
'''n=int(input("Enter a number:"))
while n>=1:
    if n%2==0:
        print(n)
    n-=1'''
#Sum of First N Odd Numbers (Using for loop)
'''n=int(input("enter a number:"))
sum=0
for i in range(1,n+1,2):
    sum+=i
print(sum)'''
#Count Digits in a Number (Using while loop)
'''n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count+=1
print("The count is:",count)'''
#Find the LCM of Two Numbers (Using while loop)
'''a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
maxnum=max(a,b)
while(True):
    if maxnum%a==0 and maxnum%b==0:
        lcm=maxnum
        break
    maxnum+=1
print(lcm)'''
#Check if a Number is Perfect(Using for loop)
'''n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Perfect number")
else:
    print("not a perfect number")'''
#Check if a Number is Armstrong (Using for loop)
'''n=int(input("Enter a number:"))
temp=n
d=len(str(n))
sum=0
for i in range(1,n+1):
    rem=n%10
    sum=sum+rem**d
    n=n//10
if sum==temp:
    print("Armstrong")
else:
    print("not Armstrong")'''

#21,22,29



    

  
    


            
