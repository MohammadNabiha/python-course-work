#system module
'''import sys
print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
sys.exit()
print("End")'''
#platform
'''import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''
#math
'''import math
print(math.e)
print(math.sqrt(16))
print(math.pow(2,3))
print(math.ceil(-12.0000000001))
print(math.ceil(-12.3))
print(math.ceil(-12.6))
print(math.ceil(-12.999999))
print(math.floor(-12.0000000001))
print(math.floor(-12.3))
print(math.floor(-12.6))
print(math.floor(-12.999999))
print(math.fabs(-123))
print(math.factorial(6))
print(math.gcd(44,12))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(190))
print(math.radians(190))
'''
#Random
'''import random
random.seed(12)#generate same output everytime
print(random.random())
print(random.randint(1,3))
print(random.uniform(1,3))#float value
l=["python","java","c++","c","html"]
print(random.choice(l))
print(random.choices(l,k=2))
print("Before:",l)
random.shuffle(l)
print("After:",l)'''
#collections
'''import collections
s='python programming'
s=[1,2,3,5,6,1,2,3,4,1,1,1,1,2,3,4,]
print(collections.Counter(s))
d=collections.defaultdict(int)
for i in s:
        d[i]+=1
print(d)
d=collections.deque([])
d.appendleft(10)
d.appendleft(20)
d.pop()
d.appendleft(30)
d.pop()
d.pop()
d.appendleft(40)
d.appendleft(50)
print(d)'''
#itertools
'''from itertools import combinations,permutations
print(list(combinations('ABCD',2)))
print(list(permutations('ABCD',3)))'''









































