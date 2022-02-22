import numbers


class calculator:

    def __init__(self,number):
      self.num = number
    def square(self):
        print(f"The value of {self.num} square is {self.num**2}")
    def squareRoot(self):
        print(f"The value of {self.num} square is {self.num**0.5}")
    def cube(self):
        print(f"The value of {self.num} square is {self.num**3}")


a = calculator(8)
a.square()
a.cube()
a.squareRoot()