import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    os.system('cls')
    choice = input(f"What would you like ? {menu.get_items()} : ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif choice == "off":
        break
    menuItem = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(menuItem):
        if money_machine.make_payment(menuItem.cost):
            coffee_maker.make_coffee(menuItem)
