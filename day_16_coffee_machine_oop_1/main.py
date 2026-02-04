from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()

coffee_machine = CoffeeMaker()
money_machne = MoneyMachine()

# Prompt the user
while True:
    query = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # To print resources
    if query == 'report':
        coffee_machine.report()
        money_machne.report()
    
    # Turn off machine
    elif query == 'off':
        break

    # To give user a coffee or feedback
    elif MENU.find_drink(query):
        item = MENU.find_drink(query)
        if coffee_machine.is_resource_sufficient(item):
            if money_machne.processing_coins(item.cost):
                coffee_machine.make_coffee(item)


