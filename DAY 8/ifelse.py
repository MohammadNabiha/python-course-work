#Battery alert
'''ch=int(input("Enter the battery per:"))
if ch<=20:
    print("Alert:Battery is low")'''
#discount 
'''discount=int(input("Enetr the discount:"))
price=int(input("Enter the price:"))
if discount:
    price-=price*(discount/100)
    print("Dicount applied")
print("Price:",price)'''
#login
'''data={
    'niharika@gmail.com':'ni@123',
    'charan@gmailk.com':'ch@123',
    'pavitra@gmail.com':'pa@123',

}
email=input("Enter the email:")
password=input("Enter the password:")
if data.get(email)==password:
    print("Login Successful")
else:
    print("Login invaid")'''
#OTP verification
'''import random
otp=random.randint(1111,9999)
print("Your OTP:",otp)
entered_otp=int(input("Enter the OTP:"))
if otp==entered_otp:
    print("Verified successfully")
else:
    print("invalid OTP")'''
#order fare
'''hr,min=list(map(int,input("Enter the time(HH:MM):").split(':')))
fare=0
price=350
if 0<=hr<=23 and 0<=min<=59:
    if 8<=hr<16:
        fare=40
    elif 17<=hr<=23:
        fare=100
    elif 0<=hr<=7:
        fare=150
    print("Totl Fare:",fare+price)
else:
    print("Invalid Time")'''
data={
