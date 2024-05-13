from logo import art
print(art)

print("Welcome to the Secret Auction Program.")
choice = 'yes'
auction = {}

def bidding_book(auction):
    highest_bid = 0
    winner_name = ""
    for winner in auction:
        value = auction[winner]
        if highest_bid < value:
            highest_bid = value
            winner_name = winner
    print(f"The winner is {winner_name} with a bid of ₹{highest_bid}!")

while choice == 'yes':
    name = input("What is your name? ")
    bid = int(input("What is your bid? ₹"))
    auction[name] = bid
    choice = input("are there any other bidders? Type 'yes' or 'no'. ")
    if choice == 'no':
        bidding_book(auction)


            

     



