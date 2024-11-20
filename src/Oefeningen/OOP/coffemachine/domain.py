class CoffeeMachine:
    type_of_coffee = {"espresso": {"Water": 50, "Milk": 30, "Coffee": 20, "Cost": 2.5},
                      "latte": {"Water": 50, "Milk": 30, "Coffee": 20, "Cost": 2.5},
                      "cappuccino": {"Water": 50, "Milk": 30, "Coffee": 20, "Cost": 2.5}
                      }

    def __init__(self, ingredient, money):
        self.coffee_ingredients = ingredient
        self.money_machine = MoneyMachine(money=money)

    def start_coffee(self):
        running = True
        while running:
            selected_coffee = input("What would you like? (espresso/latte/cappuccino):")
            if selected_coffee.lower() == 'x':
                running = False
            elif selected_coffee.lower() == 'r':
                print(self.coffee_ingredients)
            else:
                if self.type_of_coffee.get(selected_coffee) is not None:
                    if self.coffee_ingredients.checkAviable(self.type_of_coffee.get(selected_coffee)):
                        quarter = int(input('Quaters '))
                        dimes = int(input('Dimes '))
                        nickles = int(input('Nicks '))
                        pennies = int(input('Pennies '))

                        if self.money_machine.pay_total_customer_money(quarter, dimes, nickles, pennies,
                                                                       self.type_of_coffee.get(selected_coffee).get(
                                                                           "Cost")):
                            self.coffee_ingredients.subtractIngretients(self.type_of_coffee.get(selected_coffee))
                            print(
                                f"U heeft een {selected_coffee} gekocht voor{self.type_of_coffee.get(selected_coffee).get(
                                    "Cost")}")
                    else:
                        print("Sorry, we don't have enough ingredients")
                else:
                    print(f"Sorry {selected_coffee} is not available")


class MoneyMachine:
    type_of_count = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self, money):
        self.money_vault = MoneyVault(money=money)

    def pay_total_customer_money(self, quarter, dimes, nickles, pennies, to_pay_befrage):
        tot = (quarter * self.type_of_count.get("quarters") + dimes * self.type_of_count.get(
            "dimes") + nickles * self.type_of_count.get("nickles") + pennies * self.type_of_count.get("pennies"))
        if (to_pay_befrage < tot):
            pass
        if (to_pay_befrage >= tot):
            money = self.money_vault.money = self.money_vault.money - tot
            return True


class MoneyVault:
    def __init__(self, money):
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__coffee = money


class Ingredients:
    def __init__(self, water, milk, coffee):
        self.__water = water
        self.__milk = milk
        self.__coffee = coffee

    def checkAviable(self, ing: dict):
        water = ing.get("Water")
        milk = ing.get("Milk")
        coffee = ing.get("Coffee")
        if self.__water - water <= 0 or self.__milk - milk <= 0 or self.__coffee - coffee <= 0:
            return False

        return True

    def subtractIngretients(self, ing):
        water = ing.get("Water")
        milk = ing.get("Milk")
        coffee = ing.get("Coffee")
        self.__water = self.__water - water
        self.__milk = self.__milk - milk
        self.__coffee = self.__coffee - coffee

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, water):
        self.__water = water

    @property
    def milk(self):
        return self.__milk

    @milk.setter
    def milk(self, milk):
        self.__milk = milk

    @property
    def coffee(self):
        return self.__coffee

    @water.setter
    def water(self, coffee):
        self.__coffee = coffee

    def __str__(self):
        return f"Water: {self.water}ml \n Milk: {self.milk}ml \nCoffee: {self.coffee}"
