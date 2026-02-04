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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

collected_money = 0

# check resources
def check_resources(coffee, res):
    # res -> resources
    temp = False # to process coins in other function
    result = ''
    for i in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][i] > res[i]:
            result += f"Sorry there is not enough {i}." + '\n'
    if result == '':
        # print(f"Here is your {coffee}. Enjoy!")
        for i in MENU[coffee]["ingredients"]:
            res[i] = res[i] - MENU[coffee]["ingredients"][i]
        temp = True
    return res, result, temp

# Processing coins
def processing_coins(money, price):
    """Check if user has entered enough coins"""
    total = 0
    chnge = 0
    temp = False
    print('Please insert coins.')
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total < price:
        return temp, money, chnge
    else:
        temp = True
        chnge = total - price
        money += price
        return temp, money, chnge

# Prompt the user
while True:
    query = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # To print resources
    if query == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${collected_money}")
    # Turn off machine
    elif query == 'off':
        break
    # To give user a coffee or feedback
    elif query in MENU.keys():

        # Checking resources
        resources, output, process_coins = check_resources(query, resources)
        if output == '' and process_coins:
            # Calculating money
            process, collected_money, change = processing_coins(collected_money, MENU[query]['cost'])
            if process:
                if change != 0:
                    print(f"Here is ${change} dollars in change.”")
                print(f"Here is your {query}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print(output)
