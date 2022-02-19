import random

print('''
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''')

print("Welcome to hang_an Game!\n")
name = input("Enter Your name : ")
print(f"Let's play then {name}\n")
 
words = ['film','dance','robber',
'flower','watch','classObject','lisst']
length = len(words)
print("Enter the word ")
display = '_'+word
guessed_word = random.choice(words)
