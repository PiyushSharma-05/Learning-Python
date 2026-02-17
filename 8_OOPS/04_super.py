class vehicle:
    def __init__(self): #dunder methods having __ in start
        print("Constructor of vehicle")
        print("I am a vehicle")

class car(vehicle):
    def __init__(self):
        print("Constructor of car")
        print("I am a car")

class honda(car):
   
   def __init__(self):
        super().__init__()
        print("Constructor of honda")
        print("I am a honda company car")

c=vehicle()

b=car()

a=honda()