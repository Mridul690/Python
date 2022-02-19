from tokenize import String
import sys

str = "abcdefghijklmnopqrstuvwxyz"
indnum = 0
new_str = "" 

print('''
Hello, Welcome To Ceaser Cipher Program
Please enter your word that need to be ciphered..
''')

word = input("Enter the word :").lower()
shift =int(input("Enter the shift value : "))
ende = input("Write 'encode' for Encoding and 'decode' for Decoding: ").lower()

def Encrypt(syntax , shift_num):
    global new_str 
    new_str = ""
    for letter in syntax:
        indnum = str.index(letter)
        if indnum == (len(str)-1):
            indnum = -1
        indnum += shift_num
        if indnum > 25:
            indnum = indnum-26
        
        new_str = new_str + str[indnum]
    print("Encoded String :",new_str)


def Decrypt(syntax,shift_num):
    global new_str
    new_str = "" 
    for letter in syntax:
        indnum = str.index(letter)
        if indnum == 0:
            indnum = len(str)
        indnum -= shift_num
        if indnum < 0:
            indnum += 26

        new_str += str[indnum]        

    print(new_str)

if ende == "encode":
    Encrypt(word,shift)
elif ende == "decode":
    Decrypt(syntax=word,shift_num=shift)
else:
    print("Please Enter the correct choice .")
    sys.exit()

#file = open('caser.txt','a')
with open('caser.txt','a') as file:
    file.write("Entered Word :"+word + "\n")
    if ende == "encode":
        file.write("Encoded Word :" + new_str+"\n")
    else :
        file.write("Decoded Word :" + new_str+"\n")
    
    #file.read('caser.txt')
    file = open('caser.txt','r')
    print(file.read())