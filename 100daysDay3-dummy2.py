pizza_size = str(input("which size of pizza do you want? : "))
print(pizza_size)
if pizza_size == "small":
    bill = 15
    print("your pizza bill is: ",bill)
    
elif pizza_size == "medium":
    bill = 20
    print("your pizza bill  is : ",bill)
else:
    bill = 25
    print("your pizza bill is : ",bill)
ppizza =str(input("do you want ppizza?  y or n :"))
if ppizza == "y":
    if pizza_size == "small":
        bill +=2
        print("your ppizza bill is : ",bill)
    else:
        bill+=3
        print("your ppizza bill is: ",bill)
else:
    print("your pizza bill is",bill)

cheese=str(input("do you want extra or not y or n: "))
if cheese == "y" :
    bill+=1  
    print("final bill is: ",bill)
else:
    print("final bill with out cheese: ",bill)

