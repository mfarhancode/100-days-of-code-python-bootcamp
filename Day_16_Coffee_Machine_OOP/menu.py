class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

class Menu:
    def __init__(self):
        self.menu = [
        MenuItem('espresso', 1.5, {"water": 50, "coffee": 18},),
        MenuItem('latte', 2.5, {"water": 200, "milk": 150,  "coffee": 24}),
        MenuItem('cappuccino', 3.0, {"water": 250, "milk": 100, "coffee": 24},)
        ]
    
    def get_items(self):
        '''returns the names of items in menu'''
        menu_items_names = []
        for menu_item in self.menu:
            menu_items_names.append(menu_item.name)
        
        return menu_items_names
    
    def find_drink(self, order_name):
        '''returns menu item object if item is available in menu, else return None'''
        for menu_item in self.menu:
            if menu_item.name == order_name:
                return menu_item
        return None
            


