import art
bids = {}
more_bids = False

print(art.logo)

while more_bids is False:
    name = input("What is your name?")
    price= input("how much would you like to bid?")
    bids[name] = int(price)

    valid_input = False

    while valid_input is False:
        another_bidder = input("do you want to bid? Y or N")
        if another_bidder == "Y":
            valid_input = True
            print("\n" * 20)
        elif another_bidder == "N":
            valid_input = True
            more_bids = True
        else:
            print("invalid input try again")

highest_bid = 0
winner = ""

for (name,price) in bids.items():
    if price > highest_bid:
        highest_bid = price
        winner = name
print(f"The winner is {winner} with a bid of ${highest_bid}.")











# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary




