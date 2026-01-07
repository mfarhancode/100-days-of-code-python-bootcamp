class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    
    def is_resource_sufficient(self, drink):
        # drink parameter is the menuitem object
        can_make = True
        for name, qty in drink.ingredients.items():
            # print(name, qty)
            if qty > self.resources[name]:
                print(f"Sorry there is not enough {name}.")
                can_make = False
        
        return can_make
            
    def make_coffee(self, order):
        '''Parameter order: (MenuItem) The MenuItem object to make.
            Deducts the required ingredients from the resources.'''

        for name, qty in order.ingredients.items():
            self.resources[name] -= qty

        print(f"Here is your {order.name} ☕️. Enjoy!")
                