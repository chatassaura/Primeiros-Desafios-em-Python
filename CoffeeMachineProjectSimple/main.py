# 3 sabores -
# café expresso(espresso) -  latte                - caputtino
#   50 ml water                   200ml watter        250 ml watter
#   18g coffee                    24g coffee          24g coffee
#                                 150ml milk          100ml milk

# maquina cafe - max 300ml water / 200 milk / 100g coffee

# precisa de moeda
# penny 1 cent
# dime 10 cents
# nickel 5 cents
# quarter 25cents


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_coins(cost_money):
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    c_sum = (quarter * 25) + (nickles * 5) + (dimes * 10) + pennies
    total = c_sum / 100
    change = total - cost_money
    if total >= cost_money:
        return f"Here is your change: ${round(change, 2)}"

    else:
        return False


def machine_options(c_resources, c_menu):
    order_turn = True
    while order_turn:
        ask = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if ask == 'report':
            print(f"Water: {c_resources['water']}")
            print(f"Milk: {c_resources['milk']}")
            print(f"Coffee: {c_resources['coffee']}")
            print(f"Money: ${c_resources['money']}")
        elif ask in c_menu:
            order = c_menu[ask]
            ingredients = order['ingredients']
            if c_resources['water'] >= ingredients['water']:
                buy = True
            else:
                missing = 'watter'
                buy = False

            if ask != "espresso" and buy is not False:
                if c_resources['milk'] >= ingredients['milk']:
                    buy = True
                else:
                    missing = 'milk'
                    buy = False

            if buy is not False:
                if c_resources['coffee'] >= ingredients['coffee'] and buy is not False:
                    buy = True
                else:
                    missing = 'coffee'
                    buy = False

            if buy:
                enough_coins = check_coins(order["cost"])
                if not enough_coins:
                    print("Sorry that's not enough money, Money Refunded")
                else:
                    print(enough_coins)
                    c_resources['money'] += order["cost"]
                    c_resources['water'] -= ingredients['water']
                    if ask != 'espresso':
                        c_resources['milk'] -= ingredients['milk']
                    c_resources['coffee'] -= ingredients['coffee']
                    print(f"Here is your {ask}, Enjoy! :) ")
            else:
                print(f"Sorry, that's not enough {missing}")


machine_options(resources, MENU)

# Print report - mostrar resources - water  milk coffee money


## perguntar o que ele quer
# perguntar quantas moedas de cada uma#
# verificar se é suficiente as moedas e recursos
# processar moedas
# se for insuficiente, informar e dar refound
# se for suficiente, calcular e devolver o troco
# fazer café
