#flavours = input("what would you like?(espresso/latte/cappuccino:")

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
    "water": 25,
    "milk": 200,
    "coffee": 100,
}

for i in MENU.values():
    print(i)
    W = i["ingredients"]["water"] 
    W_r = resources["water"] 
    #M = i["ingredients"]["milk"] 
    #M_r = resources["milk"] 
    C = i["ingredients"]["coffee"] 
    C_r = resources["coffee"]
    c_type = input("which type do you want?") 
    def compare():
        if c_type == "espresso":
            if W <= W_r  and C <=C_r :
                print("take coffee")
        elif c_type == "latte" :
            if W <= W_r  and C <=C_r :
                print("enjoy your coffee")
        elif c_type == "cappuccino":
            if W <= W_r  and C <=C_r :
                print("enjoy good coffee")
            
        else:
            print("not possible")
    coffee_type(W,W_r,C,C_r)
