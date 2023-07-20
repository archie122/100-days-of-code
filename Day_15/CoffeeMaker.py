MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
}

TOTAL_MONEY = 0
CHANGE = 0

check_on = True


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${TOTAL_MONEY}")


def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def coffee_selection():
    selection = input("\tWhat would you like? (espresso/latte/cappuccino):")
    return selection


def selected_coffee(selection):
    if selection == "espresso":
        return MENU["espresso"]
    elif selection == "latte":
        return MENU["latte"]
    elif selection == "cappuccino":
        return MENU["cappuccino"]


def check_resources(resource1, resource2):
    if resource1 < resource2:
        return True
    else :
        return False


def coffee_process(coffee_choice, coffee_name):
    payment = money()
    global TOTAL_MONEY
    global CHANGE

    if payment >= coffee_choice["cost"]:

        if check_resources(resources["water"], coffee_choice["ingredients"]["water"]):
            print("Sorry, there is not enough water.")
        elif check_resources(resources["milk"], coffee_choice["ingredients"]["milk"]):
            print("Sorry, there is not enough milk.")
        elif check_resources(resources["coffee"], coffee_choice["ingredients"]["coffee"]):
            print("Sorry, there is not enough coffee.")
        else:
            resources["water"] -= coffee_choice["ingredients"]["water"]
            resources["milk"] -= coffee_choice["ingredients"]["milk"]
            resources["coffee"] -= coffee_choice["ingredients"]["coffee"]
            TOTAL_MONEY += coffee_choice["cost"]
            CHANGE = payment - coffee_choice["cost"]
            print(f"Here is ${CHANGE} in change.")
            print(f"Here is your {coffee_name}.")
    else:
        print("Sorry, that's not enough money.")

    return round(CHANGE, 2)


while check_on:
    coffee = coffee_selection()

    if coffee == "off":
        check_on = False

    elif coffee == "report":
        report()

    elif coffee == "espresso":
        coffee_type = selected_coffee("espresso")
        change_amount = coffee_process(coffee_type, "espresso")

    elif coffee == "latte":
        coffee_type = selected_coffee("latte")
        change_amount = coffee_process(coffee_type, "latte")

    elif coffee == "cappuccino":
        coffee_type = selected_coffee("cappuccino")
        change_amount = coffee_process(coffee_type, "cappuccino")