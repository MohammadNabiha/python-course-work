pin=1234
for i in range(5):
    entered_pin=int(input("Enter the pin:"))
    if entered_pin==pin:
        print("unlock the phone")
        break
    else:
        print("Invalid pin")
else:
    print("try after 60 sec.")
