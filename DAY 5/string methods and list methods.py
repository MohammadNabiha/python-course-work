Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names='srinidhi pavitra rishitha mounika'
names.split()
['srinidhi', 'pavitra', 'rishitha', 'mounika']
names.rsplit(' ',2)
['srinidhi pavitra', 'rishitha', 'mounika']
names.split('a')
['srinidhi p', 'vitr', ' rishith', ' mounik', '']
names.partition(' ')
('srinidhi', ' ', 'pavitra rishitha mounika')
'1.python.png'.partition('.')
('1', '.', 'python.png')
'1.python.png'.rpartition('.')
('1.python', '.', 'png')
l=['sreenidhi','pavitra','nabiha','sreeja']
''.join(l)
'sreenidhipavitranabihasreeja'
'-'.join(l)
'sreenidhi-pavitra-nabiha-sreeja'
','.join(l)
'sreenidhi,pavitra,nabiha,sreeja'
h='    xxxxxx xxxxxx   '
h.strip()
'xxxxxx xxxxxx'
h.lstrip()
'xxxxxx xxxxxx   '
h.rstrip()
'    xxxxxx xxxxxx'
'hello'.encode()
b'hello'
b'hello'.decode()
'hello'
text='Hello @@'
text.encode()
b'Hello @@'
text='🤣 🤣 🤣 (Rolling on the floor)'
text.encode()
b'\xf0\x9f\xa4\xa3 \xf0\x9f\xa4\xa3 \xf0\x9f\xa4\xa3 (Rolling on the floor)'
b'\xf0\x9f\xa4\xa3 \xf0\x9f\xa4\xa3 \xf0\x9f\xa4\xa3 (Rolling on the floor)'.decode()
'🤣 🤣 🤣 (Rolling on the floor)'
names='srinidhi pavitra rishitha mounika'
'python'.startswith('p')
True
'python.py'.endswith('.py')
True
'sdfg'.isalpha()
True
'sowm123'.isalpha()
False
'123dsfghj'.isalpha()
False
'fghg'.isalnum()
True
'1234'.isalnum()
True
'ab12'.isalnum()
True
'ab    12'.isalnum()
False
'rghj'.islower()
True
'GTRG'.isupper()
True
'    '.isspace()
True
'     j     '.isspace()
False
'rghj jhgy ghjt'.istitle()
False
'Rhju Rtyu'.istitle()
True
'myvar'.isidentifier()
True
'my@@@var'.isidentifier()
False
'45678'.isdecimal
<built-in method isdecimal of str object at 0x0000029BDEC278A0>
9
9



'45678'.isdecimal()
True
'5678'.isnumeric()
True
'5678'.isdigit()
True
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
#list is ordered
l=[1,1,1,1,]
l
[1, 1, 1, 1]
#list allows duplicates
l='fdgh',1,2.31,[1,2,3],(1,2),3+2j,True)
SyntaxError: unmatched ')'
l=['fdgh',1,2.31,[1,2,3],(1,2),3+2j,True]
l
['fdgh', 1, 2.31, [1, 2, 3], (1, 2), (3+2j), True]
#list is heterogeneous-multiple datatypes are allowed
l=['srinidhi', 'pavitra', 'rishitha', 'mounika']
l[0]
'srinidhi'
l[1]
'pavitra'
l[2]
'rishitha'
l[3]
'mounika'
l[-1]
'mounika'
l[-2]
'rishitha'
l*3
['srinidhi', 'pavitra', 'rishitha', 'mounika', 'srinidhi', 'pavitra', 'rishitha', 'mounika', 'srinidhi', 'pavitra', 'rishitha', 'mounika']
a=['1','2','3]
   
SyntaxError: unterminated string literal (detected at line 1)
l
   
['srinidhi', 'pavitra', 'rishitha', 'mounika']
l[:3]
   
['srinidhi', 'pavitra', 'rishitha']
l[3:]
   
['mounika']
l[::-1]
   
['mounika', 'rishitha', 'pavitra', 'srinidhi']
l[-4:-2]
   
['srinidhi', 'pavitra']
a=['1','2','3']
   
b=['4','5','6']
   
a+b
   
['1', '2', '3', '4', '5', '6']
l[::2}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
l[::2]
   
['srinidhi', 'rishitha']
'sreeja' in l
   
False
'nabiha' in l
   
False
l=['srinidhi', 'pavitra', 'rishitha', 'mounika']
   
'nabiha' in l
   
False
l=[]
   
l=list()
   
l=['srinidhi', 'pavitra', 'rishitha', 'mounika']
   
id(l)
   
2868436201280
l[0]='nabiha'
   
l
   
['nabiha', 'pavitra', 'rishitha', 'mounika']
id(l)
   
2868436201280
#afdterv updating also memory reference is same so list is mutable
   
l.append('sravani')
   
l
   
['nabiha', 'pavitra', 'rishitha', 'mounika', 'sravani']
l.insert(1,'Saniya')
   
l
   
['nabiha', 'Saniya', 'pavitra', 'rishitha', 'mounika', 'sravani']
l.extend(['charan','dhanush','sahil'])
   
l
   
['nabiha', 'Saniya', 'pavitra', 'rishitha', 'mounika', 'sravani', 'charan', 'dhanush', 'sahil']
l.remove('Sravani')
   
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    l.remove('Sravani')
ValueError: list.remove(x): x not in list
l.remove('sravani,)
         
SyntaxError: unterminated string literal (detected at line 1)
l.remove('sravani')
         
l.pop(0)
         
'nabiha'
l.pop()
         
'sahil'
l
         
['Saniya', 'pavitra', 'rishitha', 'mounika', 'charan', 'dhanush']
del l[0]
         
l
         
['pavitra', 'rishitha', 'mounika', 'charan', 'dhanush']
sorted(l)
         
['charan', 'dhanush', 'mounika', 'pavitra', 'rishitha']
max(l)
         
'rishitha'
min(l)
         
'charan'
len(l)
...          
5
>>> l=['srinidhi', 'pavitra', 'rishitha', 'mounika']
...          
>>> l.index('mounika')
...          
3
>>> l.index('z')
...          
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l.index('z')
ValueError: list.index(x): x not in list
>>> l.count('pavitra')
...          
1
>>> l.sort()
...          
>>> l
...          
['mounika', 'pavitra', 'rishitha', 'srinidhi']
>>> l.reverse()
...          
>>> l
...          
['srinidhi', 'rishitha', 'pavitra', 'mounika']
>>> l=[1,2,3,12]
...          
>>> m=l
...          
>>> m
...          
[1, 2, 3, 12]
>>> l
...          
[1, 2, 3, 12]
>>> n=l.copy()
...          
>>> n.append(10)
...          
>>> n
...          
[1, 2, 3, 12, 10]
>>> l
...          
[1, 2, 3, 12]
