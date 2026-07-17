Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
for i in s:
    print(i)

    
p
y
t
h
o
n
 
p
r
o
g
r
a
m
m
i
n
g
l=[1,2,3,4,5]
for i in l:
    print(i)

    
1
2
3
4
5
t=(1,2,3,4,5,6)
for i in t:
    print(i)

    
1
2
3
4
5
6
s={1,2,3,4}
for j in s:
    print(j)

    
1
2
3
4
d={1:2,3:4,5:6}
for i in d:
    print(i)

    
1
3
5
for i in d:
    print(i,d[i])

    
1 2
3 4
5 6
s='Python'
for i in enumerate(s):
    print(i)

    
(0, 'P')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
t=(1,2,3,4)
t[0]
1
t[1]
2
t[2]
3
for i in enumerate(t):
    print(i[0],i[1])

    
0 1
1 2
2 3
3 4
for i in enumerate(s):
    print(i[0],i[1])

    
0 P
1 y
2 t
3 h
4 o
5 n
l=[1234,5678,9012,5690]
for i in enumerate(l):
    print(i[0],i[1])

    
0 1234
1 5678
2 9012
3 5690
for i in enumerate(l):
    print(i[0],i[1],i)

    
0 1234 (0, 1234)
1 5678 (1, 5678)
2 9012 (2, 9012)
3 5690 (3, 5690)
for i in enumerate(t):
    print(i[0],i[1],i)

    
0 1 (0, 1)
1 2 (1, 2)
2 3 (2, 3)
3 4 (3, 4)
s={567,4567,3456}
for i in enumerate(s):
    print(i[0],i[1],i)
    
SyntaxError: multiple statements found while compiling a single statement
s={567,4567,3456}
for i in enumerate(s):
    print(i[0],i[1],i)
    
SyntaxError: multiple statements found while compiling a single statement
s={567,3456,1243,5647}
for i in enumerate(s):
    print(i[0],i[1],i)

    
0 3456 (0, 3456)
1 1243 (1, 1243)
2 567 (2, 567)
3 5647 (3, 5647)
d={'k1':'v1','k2':'v2','k3':'v3'}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]],i)

    
0 k1 v1 (0, 'k1')
1 k2 v2 (1, 'k2')
2 k3 v3 (2, 'k3')
for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
for i in range(2,21,2):
    print(i,end=' ')

    
2 4 6 8 10 12 14 16 18 20 
for i in range(5,51,5):
    print(i)

    
5
10
15
20
25
30
35
40
45
50
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(1,100,2):
    print(i,end='')

    
13579111315171921232527293133353739414345474951535557596163656769717375777981838587899193959799
for i in range(1,100,2):
    print(i,end=' ')

    
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
s='python'
len(s)
6
for i in range(len(s)):
    print(i,s[i])

    
0 p
1 y
2 t
3 h
4 o
5 n
>>> l=['niharika','sreeja','pavitra','srinidhi','sravani']
>>> for i in range(len(l)):
...     print(i,l[i])
... 
...     
0 niharika
1 sreeja
2 pavitra
3 srinidhi
4 sravani
>>> for i in range(len(t)):
...     print(i,t[i])
... 
...     
0 1
1 2
2 3
3 4
>>> t=('niharika','sreeja','pavitra','srinidhi','sravani')
>>> for i in range(len(t)):
...     print(i,t[i])
... 
...     
0 niharika
1 sreeja
2 pavitra
3 srinidhi
4 sravani
>>> t={'niharika','sreeja','pavitra','srinidhi','sravani'}
>>> t[0]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    t[0]
TypeError: 'set' object is not subscriptable
>>> for i in range(len(t)):
...     print(t[i])
... 
...     
Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    print(t[i])
TypeError: 'set' object is not subscriptable
