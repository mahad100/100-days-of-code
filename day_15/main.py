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
    "money":0,
}

initial_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def cost(chosen_drink):
    price = MENU[chosen_drink]["cost"]
    print(f"The cost of your {chosen_drink} is ${price:.2f}. Please insert coins.")

    while True:
        # Ask for coin insertion
        q = int(input(f"How many quarters? "))
        d = int(input(f"How many dimes? "))
        n = int(input(f"How many nickels? "))
        p = int(input(f"How many pennies? "))

        # Coin values
        quarters = 0.25
        dimes = 0.10
        nickels = 0.05
        pennies = 0.01

        # Calculate total money inserted
        inserted_coins = (q * quarters) + (d * dimes) + (n * nickels) + (p * pennies)
        print(f"Total inserted: ${inserted_coins:.2f}")

        # Check if the inserted amount is enough
        if inserted_coins < price:
            print(f"Sorry, that's not enough money. Money refunded.")
            retry = input("Would you like to try again? (yes/no): ").lower()
            if retry != "yes":
                print("Transaction cancelled.")
                return 0
        else:
            change = inserted_coins - price
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            return inserted_coins


def coffee(chosen_drink):
    """Checks if there are enough resources to make an espresso."""
    for ingredient, amount_required in MENU[chosen_drink]["ingredients"].items():
        if resources[ingredient] < amount_required:
            print(f"sorry we do not have enough {ingredient}.")
            return  False

    inserted_money = cost(chosen_drink)

    if inserted_money == 0:  # Transaction cancelled by user.
        return False

    price = MENU[chosen_drink]["cost"]

    if inserted_money < price:
        print(f"Sorry, that's not enough money. Money refunded.")
        cost(chosen_drink)
    else:
        for ingredient, amount_required in MENU[chosen_drink]["ingredients"].items():
            resources[ingredient] -= amount_required

        resources["money"] += price
        print(f"enjoy your {chosen_drink}!!")
        return True




    return True


def print_report():
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {value}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {value}g")
        elif key == "money":
            print(f"{key.capitalize()}: £{value:.2f}")

def restock():
    for key,value in initial_resources.items():
        resources[key] += value






while True:
    drink = input("Helloo what would you like to drink today? (espresso/latte/cappuccino)")
    if drink in MENU:
        coffee(drink)
    elif drink == "report":
        print_report()
    elif drink == "restock":
        restock()
    elif drink == "off":
        print("We are closed \nSee you tomorrow!")
        break
    elif drink not in MENU:
        print("Sorry, we don't have that drink.")







