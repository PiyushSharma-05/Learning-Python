class calculator():

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"square is: {self.n**2}")        
    def squareRoot(self):
        print(f"square root is: {self.n**1/2}")        
    def cube(self):
        print(f"cube is: {self.n**3}")        


a=calculator(4)
a.square()
a.squareRoot()
a.cube()