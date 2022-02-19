from pickle import NONE
import random

def gameWin(comp,u):
    if(comp == u):
       return NONE
    elif comp == 's':
        if(u == 'g'): return True
        elif(u == 'w'): return False
    elif comp == 'g' :
        if(u == 'w'): return True
        elif(u == 's'): return False
    elif comp == 'w':
        if(u == 's'): return True
        elif(u == 'g'): return False

print("Computer's Turn :=> Snake(s),Water(w) or Gun(g)\n")
u = input("Your Turn :=> Snake(s),Water(w) or Gun(g) : ")
a = random.randint(1,3)
if(a == 1) :
    comp = 's'
elif a==2 :
    comp = 'w'
elif a==3 :
    comp = 'g'

print(f"You Choose : {u}")
print(f"Computer Choose : {comp}")

b = gameWin(comp,u)
if(b == NONE):
    print("The Game is Tie\n")
elif b: 
    print("You Win!! :) \n")
else:
    print("You Lose! :( \n")
