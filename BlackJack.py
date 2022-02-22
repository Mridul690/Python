import random as r

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

def deal_cards():
  user_cards = r.sample(cards,2)
  comp_cards = r.sample(cards,2)
  #random.sample(list,n) returns n number (or list of size n)of randomly chosen elements from the given list ,string,tuple ,etc.
  print(f"Computer's Cards :[{comp_cards[0]},?]")
  print(f"User's Cards : [{user_cards}]")
  
  




deal_cards()
  
  