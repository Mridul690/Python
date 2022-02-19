'''class Number:
    def sum(self):
        return self.a+self.b

num = Number()
num.a=int(input("Enter a number\n"))
num.b=int(input("Enter a number\n"))
s = num.sum()
print(s)

'''

from enum import IntEnum
from imaplib import Int2AP, Internaldate2tuple
#from click import INT


class Employee:
    comapany = "Google"
    salary = 300
    def __init__(self) -> int:
        print("F = 12")
  #  @staticmethod
    def getsalary(dan):
        print("Salary is 122k")

dan = Employee()
print(dan.comapany)
Employee.comapany = "Microsoft"
dan.comapany = "Youtube"

print(dan.comapany)
dan.getsalary()# == dan.getsalary(dan)
#Not using self in function definition will cause an error

dan.salary = "30K"#Adding new value or attribute  
Employee.salary = 400#Variable already present and changing its value   
'''
In the above case Two attribute cases are shown
Among thetwo, instance attribute is given preference above class attribute incase of assignment and retrieval
'''
print(dan.salary)