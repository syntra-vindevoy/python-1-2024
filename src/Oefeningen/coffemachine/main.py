from coffemachine.domain import CoffeeMachine, Ingredients, MoneyVault


def main():
    money = MoneyVault(500)
    cm = CoffeeMachine(Ingredients(coffee=150, milk=100, water=500), money=100)
    cm.start_coffee()


if __name__ == "__main__":
    main()
