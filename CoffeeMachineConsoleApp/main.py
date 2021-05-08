from data import *
from replit import clear

def process_resources(drink_ingredients):
    has_water = (resources['water'] - drink_ingredients['water']) >= 0
    has_coffee = (resources['coffee'] - drink_ingredients['coffee']) >= 0
    if len(drink_ingredients.keys()) == 3:
        has_milk = (resources['milk'] - drink_ingredients['milk']) >= 0
        if has_water and has_coffee and has_milk:
            resources['water'] -= drink_ingredients['water']
            resources['coffee'] -= drink_ingredients['coffee']
            resources['milk'] -= drink_ingredients['milk']
        return get_resources_warnings(has_water, has_coffee, has_milk)
    else:
        if has_water and has_coffee:
            resources['water'] -= drink_ingredients['water']
            resources['coffee'] -= drink_ingredients['coffee']
        return get_resources_warnings(has_water, has_coffee)

def get_resources_warnings(has_water, has_coffee, has_milk = True):
    message = "Completed"
    limited_resources = []
    if not has_water:
        limited_resources.append("water")
    if not has_coffee:
        limited_resources.append("coffee")
    if not has_milk :
        limited_resources.append("milk")
    if len(limited_resources) == 1:
        message = f"Sorry there is not enough {','.join(limited_resources[0])}"
    elif len(limited_resources) > 1:
        message = f"Sorry there are not enough {','.join(limited_resources)}"

    return message


def check_inserted_coins(drink_cost):
    # insert coins
    print(f"The price of your drink: ${drink_cost}")
    print("Please, insert coins")
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickel: "))
    pennies = int(input("pennies: "))

    inserted_coins = quarters * coins["quarters"] + dimes * coins["dimes"] + nickles * coins["nickles"] + pennies * coins["pennies"]
    print(f"You have inserted ${inserted_coins:.2f}")

    if inserted_coins == drink_cost:
        return True
    elif inserted_coins > drink_cost:
        change = inserted_coins - drink_cost
        print(f"Here is your ${change:.2f} in change.")
        return True
    else:
        return False


def work():
    continue_working = True
    money = 0
    while continue_working:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif user_choice == "off":
            continue_working = False
            print("The coffee machine is turned off!")
        else:
            drink = MENU[user_choice]
            drink_ingredients = drink['ingredients']
            if process_resources(drink_ingredients) != "Completed":
                print(process_resources(drink_ingredients))
                print("No money taken!")
            else:

                if check_inserted_coins(drink['cost']):
                    money += drink['cost']
                    print(f"Here is your {user_choice}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")

work()