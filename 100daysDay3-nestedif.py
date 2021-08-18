print("welcome to roller coaster")
height = int(input("enter your height: "))
bill= 0
if height > 120:
    age = int(input("enter your age: "))
    if age < 12:
        bill= 5
        print("charge is 5$")
    elif age >=12 and age <=18:
        bill = 7
        print("charge is 7$")
    elif age >45 and age <55:
        print("no charges you can have free drive $",bill)
    else:
        bill = 12
        print("charge is 12$")
    
    print("testing...")
    photo = str(input("do you want to take a photo or not y or N"))
    if photo == "y":
        if age >45 and age <55:
            print("you have free photo copy")
        
        else:
            bill+= 3
            print("final bill is $ : ", bill)
    else:
        print("your bill without photo",bill)
else:
    print("you are not eligible to ride")