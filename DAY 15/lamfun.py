'''l=[1,2,2,3,4,5,5,6,12,23,345637,254,14325]
res=list(filter(lambda i:i%2==0,l))
print(res)'''

'''l='python programming language'
res=list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)'''

'''l=['operators','control','conditional','oops','files','exceptional']
res=list(filter(lambda i:i[0] in 'aeiouAEIOU',l))
print(res)'''

'''l=['operators','control','conditional','oops','files','exceptional']
res=list(filter(lambda i:len(i)>8,l))
print(res)'''

'''data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':12000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)'''

'''data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':12000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res={i:data[i]['price'] for i in data}
l2h=dict(sorted(res.items(),key=lambda i:i[1]))
h2l=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))
print("high to low:",h2l)
print("Low to high:",l2h)'''

'''from functools import reduce
l=[1,2,2,3,4,5,5,6,12,23,346537,254,14325]
m=['operators','control','conditional','oops','files','exceptional']
ms=reduce(lambda sum,i:sum+','+i,m)
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p,ms)
'''
'''def reels():
    r=['1........100','101.....200','201......300','301....400','401...500','501....600','601......700','701.....800']
    for i in r:
        yield i
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
def reels():
    yield "1-10 files"
    yield "11-20 files"
    yield "21-30 files"
    yield "31-40 files"
    yield "41-50 files"
    yield "51-60 files"
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

    



                
                
