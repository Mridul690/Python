logo = '''
   _____ ____  ______ ______ ______ ______   __  __          _____ _    _ _____ _   _ ______ 
  / ____/ __ \|  ____|  ____|  ____|  ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
 | |   | |  | | |__  | |__  | |__  | |__    | \  / |  /  \ | |    | |__| | | | |  \| | |__   
 | |   | |  | |  __| |  __| |  __| |  __|   | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
 | |___| |__| | |    | |    | |____| |____  | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
  \_____\____/|_|    |_|    |______|______| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______| '''

print(logo)
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
    add = 9999
    coins = {
        "quarter": 0.25,
        "dime": 0.1,
        "nickel": 0.05,
        "penny": 0.01
    }
    print("Please enter the coins")
    quarter = int(input("Quarters = "))
    dime = int(input("Dimes = "))
    nickel = int(input("Nickel = "))
    penny = int(input("Penny = "))
    amount = coins["quarter"] * quarter + coins["dime"] * dime + coins["nickel"] * nickel + coins["penny"] * penny

    while add > 0:
        if amount < 1.50:
            print("Amount is too low please add more for continuing transaction or ", end="")
            print("press 'cancel' to cancel transaction")
            move = input().lower()
            if move == "cancel":
                print("Your amount will be refunded\n")
                exit(0)
            else:
                quarter = int(input("Quarters = "))
                dime = int(input("Dimes = "))
                nickel = int(input("Nickel = "))
                penny = int(input("Penny = "))
                amount = coins["quarter"] * quarter + coins["dime"] * dime + coins["nickel"] * nickel + coins[
                    "penny"] * penny
                add = 99
        else:
            add = -99

    return amount


def lacking():
    global k
    a = False
    for k in resources:
        if resources[k] < sufficient_resources[k]:
            a = True
            break
    if not a:
        return [a]
    else:    
        return [a, k]


def coffee_choice():
    coffee_receieved = False
    global resources
    result = lacking()
    amount = process_coin()
    choice = input("What will you like to do? ").lower()

    if choice == "report":
        for key in resources:
            print(key + " :", end=' ')
            print(resources[key])
    elif choice == "order":
        print("Coffee : Espresso , Latte , Cappuccino ")
        coffee = input("Which coffee you want ? ").lower()
        for key in MENU:
            if coffee == key:
                if amount == MENU[key]["cost"] or amount > MENU[key]["cost"]:
                    if not result[0]:
                        print("Transaction Successful")
                        print("Here's your coffee")
                        coffee_receieved = True

                        for keys in resources:
                            resources[keys] = resources[keys] - MENU[key]["ingredients"][keys]
                        change_amt = amount - MENU[key]["cost"]
                        change_amt = round(change_amt)
                        if change_amt > 0:
                            print(f"Your Change is ${change_amt}")
                        else:
                            print("No Change. You entered sufficient amount")
                        print("Enjoy your coffee !!!")
                    else:
                        print("Resources not Sufficient", end='\n')
                        print(f"Please refill {result[1]}")
                        exit(0)
            
            if not coffee_receieved and key == "cappuccino":
                print("Your ordered coffee is not available",end = '\n')
                print("Please choose from the available options\n")    
    else:
        print("Please enter something meaningful")
        exit(0)


coffee_choice()