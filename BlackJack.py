import random as r
from weakref import WeakMethod

from platformdirs import user_runtime_dir

logo = '''
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
                       _/ |                
                      |__/              
'''
print(logo)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

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
    print("Both are Equal. ")
    print("It's a draw!!")
  elif user_sum < comp_sum :
    print(f"Your sum is less than Computer Cards Sum. ")
    print("You lose!!")
  elif user_sum > comp_sum :
    print("It's Your Win. ")
    print(f"You Won {bid_amount().amount}")
  elif user_sum == 21:
    print("You won. ")
    print(f"You Won {bid_amount().amount}")
  elif user_sum > 21 :
    print("You Lose")
    print(f" As your cards sum is {user_sum}. ")
  elif comp_sum > 21:
    print(f"You Won. As Computer's Cards sum is {comp_sum} greater than 21. ")
    print(f"You Won {bid_amount().amount}")
  
def deal_cards():
  global user_cards
  global comp_cards
  user_cards = r.sample(cards,2)
  comp_cards = r.sample(cards,2)
  #random.sample(list,n) : returns n number (or list of size n)of randomly chosen elements from the given list ,string,tuple ,etc.
  print(f"Computer's Cards :[{comp_cards[0]},?]")
  print(f"User's Cards : [{user_cards}]")

def draw_stand(hit,user_sum,comp_sum):
  new_card = r.choice(cards)
  flag = 1
  while flag==1:
    if new_card in user_cards:
      new_card = r.choice(cards)
    elif new_card in user_cards:
      new_card = r.choice(cards)
    else:
      flag = 0

  if hit == 'draw':
    if new_card == 11 and (21-user_sum)<21:
      new_card = 1
    user_cards.append(new_card)
  else:
    if new_card == 11 and (21-comp_sum)<21:
      new_card = 1
    comp_cards.append(new_card)
    
def play_game():
  user_sum = 0
  comp_sum = 0
  name = input("Please Enter Your name : ")
  print(f"Ok, {name} let's begin the game",end ='\n')
  bid_amount()
  deal_cards()
  if 11 in user_cards and sum(user_cards) == 21:
    user_cards.remove(11)
    user_cards.append(1)
  
  user_sum = sum(user_cards)
  for i in comp_cards:
      comp_sum +=i

    
  while user_sum < 18 :
    print("As your sum is less than 17,")
    print("Please Enter 'draw' to contiue :")
    hit = input().lower()
    draw_stand(hit,user_sum,comp_sum)
    user_sum = sum(user_cards)

  if user_sum > 18 :
    print("Will You draw another card or stand")
    hit = input().lower()
    draw_stand(hit,user_sum,comp_sum)
    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)
    Compare(user_sum,comp_sum)
  
  print("User's card :",user_cards)
  print("Computer's Card :",comp_cards)
  print(f"User's Cards Sum  = {user_sum}")
  print(f"Computer's Cards Sum = {comp_sum}")

play_game()
