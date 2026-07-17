from datetime import date,time,datetime,timedelta

'''t=date.today()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.weekday())
print(t.isoweekday())'''

'''year,month,day=list(map(int,input("enter the dob [YYYY-MM-DD]:").split('-')))
print(date(2026,12,31))'''

'''print(time(21,59,50))'''

'''n=datetime.now()
print(n.year)
print(n.month)
print(n.day)
print(n.hour)
print(n.minute)
print(n.second)'''

'''n=datetime.now()
print(n.strftime('%Y/%m/%d'))
print(n.strftime('%y/%m/%d'))
print(n.strftime('%Y/%m/%d %H:%M:%S'))
print(n.strftime('%y/%m/%d %I:%H:%M:%S %p'))
print(n.strftime(' %a %y/%m/%d %%I:H:%M:%S %p'))
print(n.strftime(' %A, %d %b %Y %I:%H:%M:%S %p'))
print(n.strftime(' %A, %d %B %Y %I:%H:%M:%S %p'))'''

n=datetime.now()
d=date.today()
a7=d-timedelta(days=120)
a15=n+timedelta(minutes=15)
print(a7)
print(a15)







