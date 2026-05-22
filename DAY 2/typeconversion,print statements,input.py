Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=3.14
type(b)
<class 'float'>
int(b)
3
str(b)
'3.14'
complex(b)
(3.14+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
bool(c)
True
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
s='python'
int(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
float(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
complex(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'h', 't', 'n', 'y', 'p', 'o'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
s='10'
int(s)
10
float(s)
10.0
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(i)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
str(l)
'[1, 2, 3, 4, 5]'
complex(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(i)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tuple(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(1, 2, 3, 4, 5)'
complex(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
list(t)
[1, 2, 3, 4, 5]
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
s={1,2,3,4,5}
int(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
str(s)
'{1, 2, 3, 4, 5}'
list(s)
[1, 2, 3, 4, 5]
tuple(s)
(1, 2, 3, 4, 5)
dict(s)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d={1:!,2:@,3:3,4:4,5:5}
SyntaxError: invalid syntax
d={1:1,2:2,3:3,4:4,5:5}
int(d)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
str(d)
'{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}'
list(d)
[1, 2, 3, 4, 5]
set
<class 'set'>
set(d)
{1, 2, 3, 4, 5}
tuple(d)
(1, 2, 3, 4, 5)
bool(d)
True
s=True
int(s)
1
float(s)
1.0
str(s)
'True'
list(s)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    list(s)
TypeError: 'bool' object is not iterable
set(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    set(s)
TypeError: 'bool' object is not iterable
tuple(s)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    tuple(s)
TypeError: 'bool' object is not iterable
complex(s)
(1+0j)
dict(s)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dict(s)
TypeError: 'bool' object is not iterable
a=10
b=10.2
c='python'
print(a,b,c)
10 10.2 python
print('a=',a,'b=',b,'c=',c,sep='')
a=10b=10.2c=python
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
10.2
c=
python
KeyboardInterrupt
print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	10.2	c=	python
print('a=',a,'b=',b,'c=',c,sep='\n\n')
a=

10

b=

10.2

c=

python
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	10.2	c=	python

print('a=',a,'b=',b,'c=',c,sep='\t',end='@@@@')
a=	10	b=	10.2	c=	python@@@@
print(f'a:{a},b:{b},c:{c}')
a:10,b:10.2,c:python
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=python
print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.20 c=python
print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=python
print('a={2} b={0} c={1}'.format(a,b,c))
a=python b=10 c=10.2
name=input()
mounika
name
'mounika'
name=input("Ente the name:")
Ente the name:sreeja
name
'sreeja'
type(name)
<class 'str'>
age=input("Enter the age:")
Enter the age:21
type(age)
<class 'str'>
age=int(input("Enter the age:"))
Enter the age:21
age
21
type(age)
<class 'int'>
gpa=float(input("Ente the gpa:"))
Ente the gpa:9.1
type(gpa)
<class 'float'>
'niharika sreeja pavitra mounika sravani'.split()
['niharika', 'sreeja', 'pavitra', 'mounika', 'sravani']
names=input("Enter the names:").split()
Enter the names:niharika sreeja pavitra mounika sravani
>>> names
['niharika', 'sreeja', 'pavitra', 'mounika', 'sravani']
>>> age=input("Enter the ages").split()
Enter the ages 21 22 2 3
>>> age
['21', '22', '2', '3']
>>> type(a)
<class 'int'>
>>> age=list(map(int,input("Enetr the ages:").split()))
Enetr the ages:21 22 23 24
>>> age
[21, 22, 23, 24]
>>> age=list(map(float,input("Enetr the ages:").split()))
Enetr the ages:21 22 23 24
>>> age
[21.0, 22.0, 23.0, 24.0]
>>> names=tuple(input("Enter the names:").split())
Enter the names:sdfg fghn hjbn fgyt
>>> names
('sdfg', 'fghn', 'hjbn', 'fgyt')
>>> names=tuple(int,input("Enter the names:").split())
Enter the names:1 2 3 4 5
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    names=tuple(int,input("Enter the names:").split())
TypeError: tuple expected at most 1 argument, got 2
>>> names=tuple(int,input("Enter the names:").split()))
SyntaxError: unmatched ')'
>>> names=tuple(map(int,input("Enter the names:").split()))
Enter the names:1 2 3 4
>>> names
(1, 2, 3, 4)
>>> names=tuple(map(float,input("Enter the names:").split()))
Enter the names:4 5
>>> names
(4.0, 5.0)
>>> a=eval9input())
SyntaxError: unmatched ')'
>>> a=eval(input())
1,2,3
>>> a
(1, 2, 3)
>>> a=eval(input("Eneter the dict:"))
Eneter the dict:{1:2,3:4}
>>> a
{1: 2, 3: 4}
