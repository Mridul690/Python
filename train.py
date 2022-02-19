

from functools import total_ordering


class Train:
    total_seats = int(input("Enter the number of seats available : "))

    def __init__(self,name,trname,fare,seat_no) -> None:
        self.customer_name = name
        self.train_name = trname
        self.amt = fare
        self.seat_no = seat_no
         
    def bookTicket(self):
        if(self.seat_no>self.total_seats):
            print("Seat Not Available !!! \nPlease Choose from available seats\n ")
        else:
            print("Seat is available\n Please procced to payment section to book the ticket\n ")
           
    def getStatus(self):
        print(f"\n.........Name : {self.customer_name}.........\n ")
        print(f".........Train : {self.train_name}..........\n")
        print(f"Seats Available : {self.total_seats}\n")
        print(f"Seat Number : {self.seat_no}\n")
        

    def getFare(self):
        print(f"Total Cost : Rs. {self.amt}\n")

name  = input("\nEnter Your name : ")
trname = input("Enter the train name : ")
fare = input("Enter the seat amount : ")
seat_no = int(input("Enter Seat Number : "))

train = Train(name , trname,fare,seat_no)
train.getStatus()
train.getFare()
train.bookTicket()

    