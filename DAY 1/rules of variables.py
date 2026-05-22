Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myvar=10
>>> myvar
10
>>> Myvar=10
>>> Myvar1=10
>>> My_var1=10
>>> my@var=10
SyntaxError: can't assign to operator
>>> my var=10
SyntaxError: invalid syntax
>>> 1myvar=10
SyntaxError: invalid syntax
>>> _myvar=10
>>> if =10
SyntaxError: invalid syntax
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> 
#single line comments
>>> '''
multiple line comments'''
'\nmultiple line comments'
>>> 
=== RESTART: C:/Users/Hp/OneDrive/Desktop/python course work/1,keywords.py ===
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=b=c=d=10
>>> a
10
>>> b
10
>>> c
10
>>> d
10
>>> a,b,c,d=10,20,30,40
>>> a
10
>>> b
20
>>> c
30
>>> d
40
>>> a,b=b,a
>>> a
20
>>> b
10
>>> a,b,c,d=10
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a,b,c,d=10
TypeError: cannot unpack non-iterable int object
>>> a=10
>>> type(a)
<class 'int'>
>>> b=10.3
>>> type(b)
<class 'float'>
>>> c=2+4j
>>> type(c)
<class 'complex'>
>>> s='python'
>>> id(s)
2210652253240
>>> s='py'
>>> s
'py'
>>> id(s)
2210612531016
>>> l=[1,2,3,4]
>>> id(l)
2210653099528
>>> l.append(19)
>>> l
[1, 2, 3, 4, 19]
>>> id(l)
2210653099528
>>> s='python'
>>> s="python"
>>> s=""'gdhnvhf'""
>>> s='''vujmhm'''
>>> type(s)
<class 'str'>
>>> s
'vujmhm'
>>> l=[]
#declarartion of list
>>> l=[1,2,3,4,4]
>>> l
[1, 2, 3, 4, 4]
>>> type(l)
<class 'list'>
>>> t=(12.345678,12.45678)
>>> id(t)
2210653071496
>>> type(t)
<class 'tuple'>
>>> 1={}#declaration of set
SyntaxError: can't assign to literal
>>> l={3,6,7,8} #declaration of set
>>> s=set()
>>> type(s)
<class 'set'>
>>> type(l)
<class 'set'>
>>> d={'name':'niharika','course':'pfs','batch':53}#dictionary declaration
>>> type(d)
<class 'dict'>
>>> d=None
>>> type(d)
<class 'NoneType'>
>>> a=False
>>> type(a)
<class 'bool'>
>>> 
