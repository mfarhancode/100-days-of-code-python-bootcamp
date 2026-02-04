# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

data = {}
repeat = True
while repeat:
    name = input('What is your name? :')
    bid = int(input('What is your bid?: $ '))
    data[name] = bid
    ask = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if ask == 'yes':
        print('\n'*20)
    else:
        repeat = False
        max_bid = 0
        winner = ''
        for i in data:
            if data[i] > max_bid:
                max_bid = data[i]
                winner = i
        print(f"The winner is {winner} with a bid of ${max_bid}")


