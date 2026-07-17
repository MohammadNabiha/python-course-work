Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={1:!,2:4,3:9,4:16,5:25,6:36}
SyntaxError: invalid syntax
d={1:1,2:4,3:9,4:16,5:25,6:36}
d.keys()
dict_keys([1, 2, 3, 4, 5, 6])
d.values()
dict_values([1, 4, 9, 16, 25, 36])
d.items()
dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)])
len(d)
6
min(d)
1
max(d)
6
sorted(d)
[1, 2, 3, 4, 5, 6]
d.get(7)
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
d.setdefault(7,0)
0
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 0}
d.default(8,64)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.default(8,64)
AttributeError: 'dict' object has no attribute 'default'. Did you mean: 'setdefault'?
d.setdefault(8,64)
64
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 0, 8: 64}
d.setdefault(6,0)
36
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 0, 8: 64}
#setdefault:if key already exists then the value of the that key won't change , if the key is not there then it is gng to be added in the dictionary
#set===>unordered,mutable,unique collection of elements
s=set()
s={9,1,2,4,10,12,4567,9,23,1,1,1,1,1,2,2,2}
s
{1, 2, 4567, 4, 9, 10, 12, 23}
s=set()
s.add(1)
s
{1}
s.add(1.1)
s
{1, 1.1}
s.add('string')

s
{1, 1.1, 'string'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
#set is heterogeneous but all of them should be immutable ,mutable datatypes are not allowed
s.add((1,2,3))
s
{1, (1, 2, 3), 1.1, 'string'}
s.add(2+3j)
s
{1, 1.1, 'string', (2+3j), (1, 2, 3)}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1:1,2:1})
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.add({1:1,2:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s
{1, 1.1, 'string', (2+3j), (1, 2, 3)}
s.add(False)
s
{False, 1, 1.1, 'string', (2+3j), (1, 2, 3)}
s.add(True)
s
{False, 1, 1.1, 'string', (2+3j), (1, 2, 3)}
#we dont have any accessing method in set we need control statements ,we have membership operators
1 in s
True
2 in s
False
1.1 in s
True
1.2 not in s
True
#set has union,interjection,difference
a={1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
b={2,3,7,8,9,10}
b
{2, 3, 7, 8, 9, 10}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a&b
{2, 3}
a-b
{1, 4, 5, 6}
b-a
{8, 9, 10, 7}
#symmetric difference:combine both of them and remove common elements
a^b#symmetric difference
{1, 4, 5, 6, 7, 8, 9, 10}
{1,2}<a#subset
True
{1,2,10,11,12}<a
False
{1,2,3,4,5,6,7,8,9}>a#superset
True
{1,2}>a
False
x={1,2}
y={3,4}
x.isdisjoint(y)
True
a.isdisjoint(y)
False
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{2, 3}
a.difference(b)
{1, 4, 5, 6}
sorted(a)
[1, 2, 3, 4, 5, 6]
max(a)
6
min(a)
1
len(a)
6
sum(a)
21
21
21
a.add(80)
a.add(7)
a
{80, 1, 2, 3, 4, 5, 6, 7}
a.update({67,89,10})
a
{1, 2, 3, 4, 5, 6, 7, 67, 10, 80, 89}
a.pop()
1
a.pop()
2
a.clear()
a
set()
a.add(True)
a
{True}
a={1,2,3,4,5,6,7,67,10,80,89)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={1,2,3,4,5,6,7,67,10,80,89}
a.remove(2)
a
{1, 3, 4, 5, 6, 7, 67, 10, 80, 89}
a.remove(89)
>>> a
{1, 3, 4, 5, 6, 7, 67, 10, 80}
>>> a.discard(89)
>>> a
{1, 3, 4, 5, 6, 7, 67, 10, 80}
>>> a.discard(3)
>>> a
{1, 4, 5, 6, 7, 67, 10, 80}
>>> a.discard(3)
>>> #remove gives error when the element we want to remove is not present in the set
>>> #discard handles the error and don't give errors
>>> a.remove(3)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.remove(3)
KeyError: 3
>>> a
{1, 4, 5, 6, 7, 67, 10, 80}
>>> b
{2, 3, 7, 8, 9, 10}
>>> a.intersection_updaate(b)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.intersection_updaate(b)
AttributeError: 'set' object has no attribute 'intersection_updaate'. Did you mean: 'intersection_update'?
>>> a.intersection_update(b)
>>> a
{10, 7}
>>> b
{2, 3, 7, 8, 9, 10}
>>> b
{2, 3, 7, 8, 9, 10}
>>> c=b
>>> c.add(100)
>>> c
{2, 3, 100, 7, 8, 9, 10}
>>> b
{2, 3, 100, 7, 8, 9, 10}
>>> d=b.copy()
>>> d
{2, 3, 100, 7, 8, 9, 10}
>>> #intersection.update changes the original value into result
>>> #copy is used for shallow copy if we asign a=b then we have deep copy
>>> c.add(200)
>>> c
{2, 3, 100, 7, 8, 9, 10, 200}
