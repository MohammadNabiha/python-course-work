#match searches for the starting of the pattern
'''import re
pattern=r'[A-Z]'
text='Python version 3.13.13'
res=re.match(pattern,text)
print("Match found" if res else "Not matched")
'''
#search is for first occurance
#group is for grouping the pattern into single unit

'''import re
pattern=r'\d'
text='Python version 3.13.13'
res=re.search(pattern,text)
print(res.group() if res else "Not matched")'''

'''import re
pattern=r'[A-Z]'
text='Python version 3.13.13'
res=re.search(pattern,text)
print(res.group() if res else "Not matched")'''

#findall-->gives you list of all patterns-->{}-for the length of the pattern
'''import re
pattern=r'[0-9]{2}'
text='Python version 3.13.13'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'[a-z]{3}'
text='Python version 3.13.13'
res=re.findall(pattern,text)
print(res)'''

#finditer for finding particular index
'''import re
pattern=r'[0-9]{2}'
text='Python version 3.13.13'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())'''

#fullmatch entire string needs to be matched
'''import re
pattern=r'[0-9]{10}'
text='1234567890'
res=re.fullmatch(pattern,text)
print(res.group() if res else "Not matched")'''

#sub-->for replacing the text

'''import re
pattern=r'[0-9]{10}'
text='phone no:1234567890'
res=re.sub(pattern,'**********',text)
print(res)'''

'''import re
pattern=r'[aeiouAEIOU]'
text='python programming language'
res=re.sub(pattern,'*',text)
print(res)'''

#split--->split for multiple characters

'''import re
pattern=r'[,:-]'
text='pyt,hon,pro:gra-mming-langua:ge'
res=re.split(pattern,text)
print(res)'''


















































