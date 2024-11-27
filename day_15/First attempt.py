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
    "coffee":100,
}

def espresso():
    """Checks if there are enough resources to make an espresso."""
    for ingredient, amount_required in MENU[coffee]["ingredients"].items():
        if resources[ingredient] < amount_required:
            print(f"sorry we do not have enough {ingredient}.")
            return  # Exit early if something is missing
    print("Here's your espresso!")

def latte():
    """Checks if there are enough resources to make an espresso."""
    for ingredient, amount_required in MENU["latte"]["ingredients"].items():
        if resources[ingredient] < amount_required:
            print(f"sorry we do not have enough {ingredient}.")
            return  # Exit early if something is missing
    print("Here's your latte!")

def cappuccino():
    """Checks if there are enough resources to make an espresso."""
    for ingredient, amount_required in MENU["cappuccino"]["ingredients"].items():
        if resources[ingredient] < amount_required:
            print(f"sorry we do not have enough {ingredient}.")
            return  # Exit early if something is missing
    print("Here's your cappuccino!")



coffee = input("What would you like? (espresso/latte/cappuccino)")
if coffee == "espresso":
    espresso()
elif coffee == "latte":
    latte()
elif coffee == "cappuccino":
    cappuccino()


