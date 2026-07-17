Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#collections of characters ,immutable-memory reference can be changed
s="PYthon"
type(s)
<class 'str'>
s=""
a=a+'lang'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=a+'lang'
NameError: name 'a' is not defined
a='Python'
type(a)
<class 'str'>
a=a+'lang'
id(a)
2911212642864
a="ojlk"
id(a)
2911212624448
a=a+'lok'
id(a)
2911212624544
fname='abc"
SyntaxError: unterminated string literal (detected at line 1)
fname='abc'
lname='xyz'
fname+lname
'abcxyz'
'*'*30
'******************************'
names='nabiha madiha raffan sajid farzana"
SyntaxError: unterminated string literal (detected at line 1)
names='nabiha madiha raffan sajid farzana'
names[0]
'n'
names[9]
'd'
names[-1]
'a'
names[-1]
'a'
names[-5]
'r'
names
'nabiha madiha raffan sajid farzana'
names[0:7:1]
'nabiha '
names[0:6:1]
'nabiha'
names[:6]
'nabiha'
names[8:14]
'adiha '
names[7:13]
'madiha'
names[-9:]
'd farzana'
names[-4:]
'zana'
names[-16:-8]
'an sajid'
names[::-1]
'anazraf dijas naffar ahidam ahiban'
names[-1:-7:-1]
'anazra'
names[-1:-8:-1]
'anazraf'
names[::2]
'nbh aiarfa ai azn'
names='sreeja mounika sreenidhi rishitha'
names[1::]
'reeja mounika sreenidhi rishitha'
names[0:33:4]
'sjokri ha'
'sreeja' in names
True
'prince' not in names
True
len(names)
33
sorted(names)
[' ', ' ', ' ', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'e', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'm', 'n', 'n', 'o', 'r', 'r', 'r', 's', 's', 's', 't', 'u']
#based on the ascii values the sortng takes place
ord
<built-in function ord>
ord('a')
97
chr(99)
'c'
char(255)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    char(255)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(255
    0
    
SyntaxError: '(' was never closed
chr(255)
    
'ÿ'
max(names)
    
'u'
min(names)
    
' '
names='Niharika Pavitra Sreeja'
    
names.upper()
    
'NIHARIKA PAVITRA SREEJA'
names.lower()
    
'niharika pavitra sreeja'
names.capitalize()
    
'Niharika pavitra sreeja'
l.title()
    
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.title()
NameError: name 'l' is not defined
l='Niharika Pavitra Sreeja'
    
i.title()
    
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    i.title()
NameError: name 'i' is not defined. Did you mean: 'id'?
l.title()
    
'Niharika Pavitra Sreeja'
names.swapcase()
    
'nIHARIKA pAVITRA sREEJA'
names.casefold()
    
'niharika pavitra sreeja'
names.center(50,'_')
    
'_____________Niharika Pavitra Sreeja______________'
names.center(30,'*')
    
'***Niharika Pavitra Sreeja****'
names(40,'.')
    
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    names(40,'.')
TypeError: 'str' object is not callable
names.center(40,'.')
    
'........Niharika Pavitra Sreeja.........'
names.ljust(30,'_')
    
'Niharika Pavitra Sreeja_______'
names.rjust(30,'_')
    
'_______Niharika Pavitra Sreeja'
'_______Niharika Pavitra Sreeja'
    
'_______Niharika Pavitra Sreeja'


'5'.zfill(5)
    
'00005'
'23'.zfill(5)
    
'00023'
'2345'.zfill(5)
    
'02345'
'3245678'.zfill(2)
    
'3245678'
names
    
'Niharika Pavitra Sreeja'
names.find('N')
    
0
names.find('i')
    
1
names.find('v')
    
11
names.find('z')
    
-1
names.rfind('i')
    
12
names.rfind('a')
    
22
names.index('a')
    
3
names.rindex('a)
             
SyntaxError: unterminated string literal (detected at line 1)
names.rindex('a')
             
22

names.index('z')
             
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    names.index('z')
ValueError: substring not found
#indedx gives error when the element is not present but find gives
             
#find gives -1
...              
>>> names.count('a')
...              
5
>>> names.count('')
...              
24
>>> names.count('i")
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> names.count('i')
...             
3
>>> names
...             
'Niharika Pavitra Sreeja'
>>> names.replace('a','1')
...             
'Nih1rik1 P1vitr1 Sreej1'
>>> names.replace('i','0')
...             
'N0har0ka Pav0tra Sreeja'
>>> names.pavitra('pavitra','sravani')
...             
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    names.pavitra('pavitra','sravani')
AttributeError: 'str' object has no attribute 'pavitra'
>>> names.replace('pavitra','sravani')
...             
'Niharika Pavitra Sreeja'
>>> names.replace('aeiou','12345')
...             
'Niharika Pavitra Sreeja'
>>> names.maketrans('aeiou','12345')
...             
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> names.translate(names.maketrans('aeiou','112345'))
...             
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    names.translate(names.maketrans('aeiou','112345'))
ValueError: the first two maketrans arguments must have equal length
>>> names.translate(names.maketrans('aeiou','12345'))
...             
'N3h1r3k1 P1v3tr1 Sr22j1'
