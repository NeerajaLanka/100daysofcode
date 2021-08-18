print("welcome to roller coaster")
height =input("enter your height: ")
if height > 120:
    age = input("enter your age: ")
    if age<12:
        print("pay 5$")
    elif age >=12 and age <=18:
        print("pay 7$")
    else:
        print("pay 12$")
else:
    print("you are not eligible to ride")