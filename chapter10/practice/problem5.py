from random import randint

class Train:

    def __init__(self,trainNo) -> None:
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in trian no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Trian no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
         print(f"Ticket is booked in trian no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12399)
t.book("dhaka","mymen")
t.getStatus()
t.getFare("dhaka","mymen")