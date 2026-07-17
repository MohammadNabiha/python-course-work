Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
sum(l)
15
any([1,0.0,'',[],(),set(),{},False])
True
all([1,0.0,'',[],(),set(),{},False])
False
all([1,1.1,3,'etyyui,[1,2,3]])
     
SyntaxError: unterminated string literal (detected at line 1)
all([1,1.1,3,'etyyui',[1,2,3]])
     
True
# tuple is ordered,immutable,fixed data,allows duplicates,heterogeneous
     
t=()
     
t=tuple()
     
t=(1,2,3,4,5)
     
t
     
(1, 2, 3, 4, 5)
t
     
(1, 2, 3, 4, 5)
t.add()
     
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.add()
AttributeError: 'tuple' object has no attribute 'add'
t.add(6)
     
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.add(6)
AttributeError: 'tuple' object has no attribute 'add'
t.append(7)
     
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.append(7)
AttributeError: 'tuple' object has no attribute 'append'
t=(1,1,1,1,1)
     
t
     
(1, 1, 1, 1, 1)
t
     
(1, 1, 1, 1, 1)
t=(1,1.1,'python',[1,2,3,4],(1,2,3),{1,2,3},{1:1,2:2})
     
t
     
(1, 1.1, 'python', [1, 2, 3, 4], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
a=(1,2,4)
     
x,y,z=a
     
a
     
(1, 2, 4)
x
     
1
y
     
2
z
     
4
t=(1,2,3)
     
id(t)
     
1785207822336
t=t+(5,6)
     
id(t)
     
1785205873184
t=('charan','surya','john','lakshmi kanth','nageshwar','dhananjay')
     
t+('prince','ravi')
     
('charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'prince', 'ravi')
t*8
     
('charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay', 'charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay')
t[2]
     
'john'
t[4]
     
'nageshwar'
t[-2]
     
'nageshwar'
t[-1]
     
'dhananjay'
t[0]
     
'charan'
t[:3:]
     
('charan', 'surya', 'john')
t[-2:]
     
('nageshwar', 'dhananjay')
t[::2]
     
('charan', 'john', 'nageshwar')
t[1::2]
     
('surya', 'lakshmi kanth', 'dhananjay')
t[::-1]
     
('dhananjay', 'nageshwar', 'lakshmi kanth', 'john', 'surya', 'charan')
t
     
('charan', 'surya', 'john', 'lakshmi kanth', 'nageshwar', 'dhananjay')
t[-1:-3,-1]
     
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t[-1:-3,-1]
TypeError: tuple indices must be integers or slices, not tuple
t[-1:-4:-1]
     
('dhananjay', 'nageshwar', 'lakshmi kanth')
'charan' in t
     
True
'niharika' in t
     
False
t=(1,1,1,1,1,2,2,2,3,4,5)
     
t.count(1)
     
5
t.count(2)
     
3
t.count(3)
     
1
t.index(2)
     
5
t.index(10)
     
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
max(t)
     
5
min(t)
     
1
len(t)
     
11
sorted(t)
     
[1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5]
#sorted result will be in list format
     
sum(t)
     
23
s=[9,8,5,4,6]
     
sorted(s)
     
[4, 5, 6, 8, 9]
#this wont effect the original s value its just temporary
     
s.sort()
     
s
     
[4, 5, 6, 8, 9]
#permanent sorting
     
s=[4,8,7,20]
     
sorted(s)
     
[4, 7, 8, 20]
s
     
[4, 8, 7, 20]
#see original s is not changed
     
s.sort()
     
s
     
[4, 7, 8, 20]
original s value changed
     
SyntaxError: invalid syntax
#original value changed
     
t=(1,5,6,7)
     
t.sort()
     
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
data={}
     
type(data)
     
<class 'dict'>
data
     
{}
data={'userid':101,'username':'ravi','skills':['Python','java','sql','gpa':8.9]}
     
SyntaxError: invalid syntax
data={'userid':101,'username':'ravi','skills':['Python','java','sql'],'gpa':8.9]}
    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
data={'userid':101,'username':'ravi','skills':['Python','java','sql'],'gpa':8.9}
    
data
    
{'userid': 101, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
{'userid': 101, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
    
{'userid': 101, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
d={}
    
d[1]]'int'\
SyntaxError: unmatched ']'
d[1]='int'\


      
d[1.1]='float'
d
{1: 'int', 1.1: 'float'}
d['string']='str'
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3,4)]='tuple'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple'}
d[[1,2,3,4]]='set'
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d[[1,2,3,4]]='set'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[{1:1,2:1}]='dict'
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d[{1:1,2:1}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d[False]='bool'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple', False: 'bool'}
d[(2+3j)]='complex'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple', False: 'bool', (2+3j): 'complex'}
data['userid']=102
data
{'userid': 102, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
d={}
type(d)
<class 'dict'>
d=dict(d)
type(d)
<class 'dict'>
data+{1:1}
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    data+{1:1}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
data*2
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    data*2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
data[::1]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    data[::1]
KeyError: slice(None, None, 1)
data
{'userid': 102, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
'userid' in data
True
'age' not in data
True
dat['userid']
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    dat['userid']
NameError: name 'dat' is not defined. Did you mean: 'data'?
data['userid']
102
data['skills']
['Python', 'java', 'sql']
data['gpa']
8.9
dat['username']
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    dat['username']
NameError: name 'dat' is not defined. Did you mean: 'data'?
data['username']
'ravi'
data
{'userid': 102, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
data['age']
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    data['age']
KeyError: 'age'
data,get('username')
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    data,get('username')
NameError: name 'get' is not defined. Did you mean: 'set'?
data.get('username')
'ravi'
data.get('age')
>>> data.get('age','age is not present')
'age is not present'
>>> #get method handles the error and returns ntg when error occurs
>>> data
{'userid': 102, 'username': 'ravi', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
>>> data['username']
'ravi'
>>> id(data)
1785165618048
>>> data['username']='sahil'
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql'], 'gpa': 8.9}
>>> id(data)
1785165618048
>>> data['gpa']=10
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql'], 'gpa': 10}
>>> data['skills'].append('flask')
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql', 'flask'], 'gpa': 10}
>>> # above example is modification of list in a dictionary
>>> data['age']=21
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql', 'flask'], 'gpa': 10, 'age': 21}
>>> data.update({'phoneno':9876543210,'passedout':2026})
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql', 'flask'], 'gpa': 10, 'age': 21, 'phoneno': 9876543210, 'passedout': 2026}
>>> data.pop('age')
21
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql', 'flask'], 'gpa': 10, 'phoneno': 9876543210, 'passedout': 2026}
>>> data.popitem()
('passedout', 2026)
>>> data
{'userid': 102, 'username': 'sahil', 'skills': ['Python', 'java', 'sql', 'flask'], 'gpa': 10, 'phoneno': 9876543210}
>>> data.popitem(2)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    data.popitem(2)
TypeError: dict.popitem() takes no arguments (1 given)
>>> del data['skills']
>>> data
{'userid': 102, 'username': 'sahil', 'gpa': 10, 'phoneno': 9876543210}
>>> data.clear()
>>> data
{}
