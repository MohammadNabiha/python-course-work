#syntax of while
'''#init
while cond:
    #updation'''
#remove 0 and print the list
'''l=[1,2,0,3,0,2,0,4,5,0,2,0,4,20,2,12,0,45,12]
while 0 in l:
    l.remove(0)
print(l)'''
#print from 1 to 10
'''i=1
while i<=10:
    print(i)
    i+=1'''
#print from 100 to 2
'''i=100
while i>=2:
    print(i,end=' ')
    i-=1'''
#print the table of a given number
'''n=int(input("Enter a number:"))
i=1
while i<=10:
    print(f'{n}x{i}={n*i}')
    i+=1'''
#break and continue in while
'''i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1'''
#................................
'''i=1
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)'''
#sum of a number
'''n=int(input("Enter a number:"))
sum=0
while n>0:
    sum+=n%10
    n//=10

print("sum of digits:",sum)'''
#factorial of a number
'''n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''
#factors of a number
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)'''
#code o/p:dpef
'''n=input("Enter a string:")
res=''
for i in n:
    res+=chr(ord(i)+1)
print(res)'''
#code......3 e
#           2 d
#           1 o
 #          0 c
'''n=input("Enter a string:")
i=len(n)-1
while i>=0:
    print(i,n[i])
    i-=1'''
#first non-repeting character
'''n=input("enter a string:")
for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("all are repeating multiple times")'''
#reverse the integer
'''n=int(input("enter the number:"))
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)  '''  

    

    
   

        
      
      
