from random import randint

class train:
    @staticmethod
    def greet():
        print("Welcome to Indian Railways")

    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def book(piyush,fro,to):
        print(f"Your ticket is booked in train with train no. {piyush.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"train with train no. {self.trainNo} is running on time")        

    def getFare(self,fro,to):
        print(f"Ticket fare for train no. {self.trainNo} from {fro} to {to} is: {randint(300,500)}")    


p1=train(12390)
p1.greet()
p1.book("Rewa","Jabalpur")
p1.getStatus()
p1.getFare("Rewa","Jabalpur")