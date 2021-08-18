logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = { }
bidding_finished = False
user = input("are there other users who want to bid? yes or no?")
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if  bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
        
    print(f"the winner is {winner} with a amount{highest_bid} ") 


while not bidding_finished :
    name = input("enter your name")
    price = int(input("enter your price in $ "))       
    bids[name]=price
    should_continue=input("are there any other bidders?yes or no")           
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)      
    
        
          
        


