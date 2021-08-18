MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#print(MENU["cappuccino"]["ingredients"]["milk"])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
ask_cafe = True
def compare():
    for i in a:
   # print(a[i])
        if a[i] <= resources[i]:
            coins(money)
           
            return "take coffee"

        else:
            print( "ingrediants insufficent")
            ask_cafe = False
            return ask_cafe
def coins(money):
    P_coins = float(input("enter coins in penny: "))* 0.01 
    N_coins = float(input("enter coins in nickel: "))* 0.05
    D_coins = float(input("enter coins in dime: "))* 0.1
    Q_coins = float(input("enter coins in quater: ")) * 0.25
    total = P_coins + N_coins + D_coins +  Q_coins
    print( total )
    
    if cafe["cost"] == total:
        print("amount is sufficient")
        
    elif cafe["cost"] < total:
        total -=cafe["cost"] 
        

        print(f"the remaining change is {total}")
    else:
        print("insufficient amount")
        ask_cafe = False
        return ask_cafe

def reduce_resources():
    for i in a:
        resources[i]-=a[i]
    return resources

def profit():
    global money
    money +=cafe["cost"]
    return money  

money = 0
while ask_cafe == True:
    #print(resource)
    type_cafee = input("which flavour do you want?")
    if type_cafee == "report":
        print(resources)
        #print(resource)
        # money += cafe["cost"] 
        print(money)
    elif type_cafee == "off" :
        ask_cafe = False
    else:
        cafe = MENU[type_cafee]
        a = cafe["ingredients"]
        #print(a)
        b =  compare()
        print(b)
        resource=reduce_resources()
        m = profit() 
    
   





    

   
    

