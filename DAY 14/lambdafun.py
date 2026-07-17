'''add=lambda a,b:a+b
print(add(3,4))'''
'''add=lambda base,power:base ** power
print(add(3,4))'''
'''wish=lambda name:f'{name},welcome to python'
print(wish('sreeja'))
print(wish('sahil'))
'''
'''check=lambda num:"even" if num%2==0 else "odd"
print(check(19))
print(check(18))'''
'''square=lambda num:num**2
print(square(19))
print(square(18))'''
'''check=lambda a,b:max(a,b)
print(check(19,16))
print(check(18,14))'''
'''check=lambda a,b:a if a>b else b
print(check(19,16))
print(check(18,21))'''
'''check=lambda s: len(s)
print(check('dfhnvryjmbbyjm'))
print(check('579jbf4563jn'))'''
'''check=lambda s: "starts with vowel" if s[0] in "aeiouAEIOU" else "not starts with vowel"
print(check('dfhnvryjmbbyjm'))
print(check('e79jbf4563jn'))'''
'''check=lambda email:email.split('@')[-1]
print(check('dsefg@gmail.com'))
print(check('gyhf@yahoo.com'))
print(check('swdcxa@codegnan.com'))'''
#list,tuple,set,dict
'''check=lambda year:"Leap Year" if year%400==0 or (year%4==0 and year%100!=0) else "not leap year"
print(check(2024))
print(check(2026))'''
'''check=lambda year:year%10
print(check(2024))
print(check(2026))'''
'''l=[1,2,3,4,5,6,6]
res=list(map(lambda i:i**2,l))
print(res)'''
'''l=['hello','world','python','lambda']
res=list(map(lambda i:i.upper(),l))
print(res)'''
l={'sahil':45,'niharika':80,'mounika':65,'charan':92}
print(dict(sorted(l.items(),key=lambda i:i[1])))
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))











































