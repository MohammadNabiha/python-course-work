'''def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            yield i
num=int(input("Enter number:"))
gen=factors(num)
print(list(gen)[::-1])'''

#12--->1 2 3 4 6 12
'''def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
def generators(res):
    for i in res:
        yield i
r=factors(38)
g=generators(r)
for i in range(len(r)):
    print(next(g))'''

#reverse list
'''def generators(res):
    for i in range(len(res)-1,-1,-1):
        yield res[i]
l=eval(input("enter the list:"))
g=generators(l)
for i in range(len(l)):
               print(next(g),end=' ')'''
#even numbers using generator
'''def even(l):
    return list(filter(lambda i:i%2==0,l))
def gen(l):
    for i in l:
        yield i
l=[1,2,3,4,5,6,7,8,9,10,23,34,56,24,545]
e=even(l)
g=gen(e)
for i in range(len(e)):
    print(next(g))'''
    

