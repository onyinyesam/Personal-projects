money = 0
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
}


def resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total, 2)


def transaction_successful(inserted, order_ingredients):
    if inserted >= order_ingredients['cost']:
        global money
        money += order_ingredients['cost']
        change = inserted - order_ingredients['cost']
        print(f"Here is ${change} dollars in change")
        return True
    else:
        print("Sorry that's not enough money")
        return False


end = True

while end:
    choice = input("What would you like (espresso/latte/cappuccino): ")
    if choice == "off":
        end = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        if resource_enough(drink['ingredients']):
            cash = process_coins()
            if transaction_successful(cash, drink):
                if choice == "latte" or choice == "cappuccino":
                    resources['water'] -= drink['ingredients']['water']
                    resources['milk'] -= drink['ingredients']['milk']
                    resources['coffee'] -= drink['ingredients']['coffee']
                    print(f"Here is your {choice}")
                else:
                    resources['water'] -= drink['ingredients']['water']
                    resources['coffee'] -= drink['ingredients']['coffee']
                    print(f"Here is your {choice}")


