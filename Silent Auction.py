import os

print("#### WELCOME TO THE SILENT AUCTION PROGRAM ####")

def find_winner(winner_detalis):
    highest_bid=0
    winner_name=""
    for bidder in winner_detalis:
        bidding_price=winner_detalis[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner_name=bidder
    print(f"The bidder is {winner_name} and the price is {highest_bid}")
            
        
        
    
winner={}
no_of_time=False

while not no_of_time:
    name=input("Enter youer Name :")
    price=int(input("Enter Youer bid Price :"))
    winner[name]=price
    more_bidder=input("Are there more Bidders? 'yes' or 'no' :\n")
    if more_bidder=='no':
        no_of_time=True
        find_winner(winner)
    elif more_bidder=='yes':
        os.system('cls')
        

    
    
