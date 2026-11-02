import os

def clear_screen():
    # Clears the terminal screen for Windows (nt) or Mac/Linux (posix)
    os.system('cls' if os.name == 'nt' else 'clear')

should_continue = True

def hightest_bidder(bid_dict):
    highest_bit_amount = 0
    highest_bidder = ''
    for bid in bid_dict:
        bid_amount = bid_dict[bid]
        if highest_bit_amount < bid_amount:
            highest_bit_amount = bid_amount
            highest_bidder = bid
   
    print(f"\nMethod1: The winner is {highest_bidder} with a bid of ${highest_bit_amount}!")

bid = {}
while should_continue:
    name = input("Please enter bidder name: ")
    price = float(input("Please enter bid amount:$ "))
    bid[name] = price
    add_bidders = input('Add more bidders, type "yes" else "no"? ')
    clear_screen()
    if add_bidders == "no":
        should_continue = False 

hightest_bidder(bid)
print(f"Method2: The winner is {max(bid,key=bid.get)} with a bid of ${max(bid.values())})")
