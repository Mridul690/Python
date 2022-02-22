import random as r
from weakref import WeakMethod

logo = '''
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/              
'''
print(logo)

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
def bid_amount():
    bid = [10,50,100,500,1000]
    amount = 0
    print(f"You are to bid from {bid}\n")
    print("Please enter your bid :")
    Bidding = True
    while Bidding:
        amount += int(input())
        print("Current bidding amount :", amount) 
        choice = input("Do you want to bid more 'y' or 'n' :")
        if choice == 'n':
            Bidding = False
            print(f"Final Bidding Amount = {amount}")


def deal_cards():
  user_cards = r.sample(cards,2)
  comp_cards = r.sample(cards,2)
#  bid_amount()
  #random.sample(list,n) returns n number (or list of size n)of randomly chosen elements from the given list ,string,tuple ,etc.
  print(f"Computer's Cards :[{comp_cards[0]},?]")
  print(f"User's Cards : [{user_cards}]")
  Compare(user_cards,comp_cards)



def Compare(user_cards,comp_cards) :
    sum = 0
    for i in user_cards:
        sum = sum+i
  
    if sum <18:
        h = input("Please press 'H' for serving next card : ").upper()
        if h == 'H':
            new_card = r.choice(cards)
 
