'''name = input("Enter the name of user \n") 
print("Good Afternoon, "+name)'''

letter = '''Dear <|NAME|>,
You are selected!

Date : <|DATE|>'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)  # replace() func. Creates a duplicate string and then replaces the elements
letter = letter.replace("<|DATE|>", date)  # Making change in the original string
print(letter)
