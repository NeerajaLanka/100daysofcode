print("logo")
dict_new ={ }
bidder = input("is there any other bidders yes or no")
while bidder == "yes":
    name =input("enter your name")
    price = input("enter amount")
    def dict_values(name_key,price_values):
        #name = name_key
        #price = price_values
        dict_new[name]= price
        print(dict_new)
    dict_values(name_key=name,price_values=price)
    unknown_bidders = input("are there any unknown bidders?")   
    if  unknown_bidders == "yes":
        print("clear screen") 
    else:
        bidder = "no" 
        amount = "0"
        winner = " " 
        for i in dict_new:
            print(dict_new[i])
            if amount < dict_new[i]:
                amount = dict_new[i]
                print( amount)
                winner = i
        print(f"the winner is {winner},amount is {amount}")



