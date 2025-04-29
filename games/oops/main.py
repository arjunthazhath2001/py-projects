from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu=Menu()
coffee= CoffeeMaker()
money= MoneyMachine()

is_on= True


while is_on:

    order= input(f"Whats your choice: ({menu.get_items()})")
    if order=="off":
        is_on=False
    elif order=="report":
        coffee.report()
        money.report()
    else:
        drink= menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
            

