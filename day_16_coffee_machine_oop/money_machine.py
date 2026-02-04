class MoneyMachine:
    def __init__(self):
        self.money = 0


    def report(self):
        print(f"Money: ${self.money}")

    def processing_coins(self, price):
        """Check if user has entered enough coins"""
        total = 0
        chnge = 0
        print('Please insert coins.')
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        if total < price:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            chnge = total - price
            self.money += price
            if chnge:
                print(f"Here is ${chnge} dollars in change.”")
            return True
        
        