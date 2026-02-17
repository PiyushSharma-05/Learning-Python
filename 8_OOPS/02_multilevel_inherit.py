class vehicle:
    def show(self):
        print("I am a vehicle")

class car(vehicle):
    def show2(self):
        print("I am a car")

class honda(car):
    def show3(self):
        print("I am a honda company car")

a=honda()
a.show3()
a.show2()
a.show()        