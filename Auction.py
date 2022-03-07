import os

data = {}


def Bidders(biding_record):
    max_val = 0
    winner = ''
    for bid in biding_record:
        bid_ammount = biding_record[bid]
        if bid_ammount > max_val:
            max_val = bid_ammount
            winner = bid
    print(f"The winner is {winner} with a bid of ${max_val}")


user_continue = True
while user_continue:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    data[name] = bid
    user = input("Do you want to continue? yes or no?\n").lower()
    if user == 'no':
        user_continue = False
        Bidders(biding_record=data)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
