global resources
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

sufficient_resources = {
    "water": 50,
    "milk": 100,
    "coffee": 24
}


def process_coin():
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    add = 9999
    coins = {
        "quarter": 0.25,
        "dime": 0.1,
        "nickel": 0.05,
        "penny": 0.01
    }
    print("Please enter the coins \n")
    quarter = int(input("Quarters = "))
    dime = int(input("Dimes = "))
    nickel = int(input("Nickel = "))
    penny = int(input("Penny = "))
    amount = coins[quarter] * quarter + coins[dime] * dime + coins[nickel] * nickel + coins[penny] * penny

    while add>0:
        if amount < 1.50:
            print("Amount is too low please add more for continuing transaction or press 'cancel' to cancel transaction", end="\n")
            move = input().lower()
            if move=="cancel":
                print("Your amount will refunded\n")
            quarter = int(input("Quarters = "))
            dime = int(input("Dimes = "))
            nickel = int(input("Nickel = "))
            penny = int(input("Penny = "))
            amount = coins[quarter] * quarter + coins[dime] * dime + coins[nickel] * nickel + coins[penny] * penny
            add = 99
        else:
            add = -99

    return amount


def coffee_choice():
    global resources
    amount = process_coin()
    choice = input("What will you like to do? \n").lower()

    for key in resources:
        if resources[key] < sufficient_resources[key]:
            print("Resources are not sufficient\n")
            print(f"Please refill {key}")
            print(f"Current {key} value : {resources[key]}")

    if choice == "report":
        for key in resources:
            print(key + " :", end=' ')
            print(resources[key])
    else:
        for key in MENU:
            if choice == MENU[key]:
                if amount == MENU[key]["cost"]:
                    print("Transaction Successful")
                    print("Here's your coffee")
                    for keys in resources:
                        resources[keys] = resources[keys] - MENU[key][keys]




