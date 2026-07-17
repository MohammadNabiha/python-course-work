Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a,b,c=[10,20,30]
>>> a
10
>>> b
20
>>> c
30
>>> a,b,c=list(map(int,input("Enter the a b c values:").split()))
Enter the a b c values:2 3 4
>>> a
2
>>> b
3
>>> c
4
>>> email,password=input("enter email and password:").split()
enter email and password:nbif@gmail.com
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    email,password=input("enter email and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
>>> email,password=input("enter email and password:").split()
SyntaxError: invalid syntax
>>> 
>>> email,password=input("enter email and password:").split()
SyntaxError: invalid syntax
>>> 
>>> email,password=input("Enetr the password and email:").split()
Enetr the password and email:nnabiha676@gmail.com
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    email,password=input("Enetr the password and email:").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> email,password=input("Enetr the password and email:").split()
Enetr the password and email:abcdef@gmail.com 2345
>>> email
'abcdef@gmail.com'
>>> password
'2345'
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a//b
2
>>> 10//3
3
>>> 10/3
3.3333333333333335
>>> a%b
0
>>> a**b
100000
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> a<b
False
>>> a>=b
True
>>> a<=b
False
>>> a=40
>>> a=a+10
>>> a=a+20
>>> a
70
>>> a+=10
>>> a
80
>>> a-=30
>>> a
50
>>> a*=2
>>> a
100
>>> a//=30
>>> a
3
>>> a**=3
>>> a
27
>>> a%=4
>>> a
3
>>> a/==2
SyntaxError: invalid syntax
>>> a/=2
>>> a
1.5
>>> a=6
>>> a%2==0 and a%3==0 and a%6==0
True
>>> a=12
>>>  a%2==0 and a%3==0 and a%6==0
SyntaxError: unexpected indent
>>> 
>>> a=12
>>> a%2==0 and a%3==0 and a%6==0
True
>>> a=32
>>> a%2==0 and a%3==0 and a%6==0
False
>>> a=12
>>> a%2==0 or a%3==0 or a%6==0
True
>>> a=47
>>> a%2==0 or a%3==0 or a%6==0
False
>>> a%2==0
False
>>> not a
False
>>> nnot a%2=0
SyntaxError: invalid syntax
>>> not a%2=0
SyntaxError: can't assign to operator
>>> not a%2==0
True
>>> #str,list,tuple,set,dict
>>> 'p' in 'python'
True
>>> 'u'in 'python'
False
>>> 'i' not in 'python'
True
>>> l=[1,2,3,4]
>>> 4 in l
True
>>> 2 in l
True
>>> 9 not in l
True
>>> 8 in l
False
>>> 1 not in l
False
>>> t=(80,70,60)
>>> 60 in t
True
>>> 100 not in t
True
>>> s={2,5,7,8,9}
>>> 7 in s
True
>>> 15 not in s
True
>>> 9 not in s
False
>>> #membership operators only looks for the keys in the dictionary
>>> d={1:1,2:4,3:9,4:8,5:10}
>>> 6 in d
False
>>> 2 in d
True
>>> 4 in d
True
>>> True
True
>>> a=[1,2,3,4]
>>> b=[1,2,3,4]
>>> a==b
True
>>> a is b
False
>>> c=a
>>> c
[1, 2, 3, 4]
>>> a==c
True
>>> a is c
True
>>> id(a)
1702291528136
>>> id(b)
1702291471496
>>> id(c)
1702291528136
>>> a is not c
False
>>> a is not b
True
>>> e=[]
>>> id(e)
1702291170824
>>> e=d
>>> id(e)
1702290867256
>>> a is e
False
>>> 10& 11
10
>>> 7&13
5
>>> 8<<1
16
>>> #left shit:*2
>>> 16<<1
32
>>> #left shift adding zeroes 9-1001 9>>1--->10010
>>> 9>>1
4
>>> 9<<1
18
>>> 7
7
>>> 7|13
15
>>> 7^13
10
>>> 8<<1
16
>>> 
