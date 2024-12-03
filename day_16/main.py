from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

on = True
while on:
    drink = input(f"What would you like? ({menu.get_items()})")
    if drink == "report":
        coffee_maker.report()
        money.report()
    elif drink == "off":
        on = False
    elif drink == "price":
        for item in menu.menu:  # Assume menu.menu contains the list of MenuItem objects
            print(f"{item.name.title()}: ${item.cost:.2f}")
    else:
        order = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                coffee_maker.make_coffee(order)







