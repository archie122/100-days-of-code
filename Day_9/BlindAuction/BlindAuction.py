from replit import clear
from art import *


# HINT: You can call clear() to clear the output in the console.

def find_largest_bidder(bidding_dict):
    highest_bid = 0
    bidder = ""
    for key in bidding_dict:
        if highest_bid < bidding_dict[key]:
            highest_bid = bidding_dict[key]
            bidder = key

    print(f"The winner is {bidder} with a bid of ${highest_bid}")


bidding_dict = {}
check = "yes"

while check == 'yes':
    print(logo2)
    print("Welcome to the secret auction program.")
    name = input("What is your name? : ")
    bidding = int(input("What's your bid? : $"))
    check = input("Are there any other bidders? Type 'yes' or 'no' : ")

    bidding_dict[name] = bidding

    if check == 'no':
        find_largest_bidder(bidding_dict)
    else:
        clear()