'''def greet(name):
    print(f"Hello {name},Welcome to the python")
greet("Mounika")
greet("sreeja")
greet("rishitha")
'''#positional arguments
'''
def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'phonenumber:{phonenumber}')
display("Mounika","Mounika@gmail.com","8675976854")
display("Mounika@gmail.com","Mounika","8675976854")
display("8675976854","Mounika","Mounika@gmail.com")'''
#keyword arguments
'''
def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'phonenumber:{phonenumber}')
display(name="Mounika",email="Mounika@gmail.com",phonenumber="8675976854")
display(email="Mounika@gmail.com",name="Mounika",phonenumber="8675976854")
display(phonenumber="8675976854",name="Mounika",email="Mounika@gmail.com")
'''
#Default arguments:they should always present at the end
'''def display(name,email,phonenumber=None,cgpa=None):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'phonenumber:{phonenumber}')
    print(f'cgpa:{cgpa}')
display("Mounika","Mounika@gmail.com","8675976854",8.8)
display("Mounika","Mounika@gmail.com","8675976854")
display("Mounika","Mounika@gmail.com")
'''
#variable length arguments
'''def display(*names):
    print(names)
display('charan')
display('varun','dhanush')
display('sahil','niharika','pavitra','srishanth')
display('sreeja','anjali','priyanka')
'''
'''
def display(**names):
    print(names)
display(n1='charan')
display(n2='varun',n3='dhanush')
display(n4='sahil',n5='niharika',n6='pavitra',n7='srishanth')
display(n8='sreeja',n9='anjali',n10='priyanka')
'''
#whether the number is prime or not
'''n=int(input("Enter a number:"))
count=0
for i in range(2,n//2+1):
    if n%i==0:
        count+=1
print("Prime Number" if count==0 else "Not a Prime")
 '''
#using functions check prime or not
'''def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number:"))
print("Prime Number" if isprime(n) else "Not a Prime")
'''
#check vowel,consonent,digit,space,word count
def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
    print(f"Vol Count:{vc}")
    print(f"Con Count:{cc}")
    print(f"Dig Count:{dc}")
    print(f"Word Count:{wc}")
    print(f"Space Count:{sc}")
check("python programming language: version 3.14)

