from art import calculater

print(calculater)

#Functions for Calculator
def add(a,b):
  """Returns the sum of two numbers"""
  return a+b

def subtract(a,b):
  """Returns the difference of two numbers"""
  return a-b

def multiply(a,b):
  """Returns the product"""
  return a*b

def divide(a,b):
  """Returns the division of two numbers"""
  return a/b

#Operations Dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def Calculate():
  a = float(input("Enter the operand : "))
  
  finished_calculating = False
  while not finished_calculating:
    b = float(input("Enter the next operand : "))
    n = input("Enter the operation need to performed :")
    function = operations[n]
    output = function(a,b)
    print(f"{a} {n} {b} = {output}")
    flag = input("Press 'y' to continue calculating and 'n' for exiting current process and 'c' for closing the calculator :").lower()
    if flag == 'y':
      a = output
      finished_calculating = False
    elif flag =='n':
      finished_calculating = True
      Calculate()
    else:
      finished_calculating = True
  
Calculate()