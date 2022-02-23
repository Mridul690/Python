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

global user_cards
global comp_cards

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

def Compare(user_sum,comp_sum) :
   if user_sum == comp_sum :
     print("Both are Equal ")
     print("It's a draw!!")
   if user_sum < comp_sum :
     print(f"Your sum is less than Computer Cards Sum ")
     print("You lose!!")
   if user_sum > comp_sum :
     print("It's Your Win")
     print(f"You Won {bid_amount().amount}")


def deal_cards():
  global user_cards
  global comp_cards
  user_cards = r.sample(cards,2)
  comp_cards = r.sample(cards,2)
  #random.sample(list,n) : returns n number (or list of size n)of randomly chosen elements from the given list ,string,tuple ,etc.
  print(f"Computer's Cards :[{comp_cards[0]},?]")
  print(f"User's Cards : [{user_cards}]")


def play_game():
  name = input("Please Enter Your name : ")
  print(f"Ok, {name} let's begin the game",end ='\n')
  








 
