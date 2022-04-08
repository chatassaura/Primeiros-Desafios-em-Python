from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    menu_itens = menu.get_items()
    ask = input(f"What would you like? ({menu_itens}): ").lower()
    if ask == "off":
        is_on = False
    elif ask == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(ask)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)

