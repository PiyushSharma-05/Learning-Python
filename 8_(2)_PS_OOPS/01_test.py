class twoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is: {self.i}i + {self.j}j")    

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The vector is: {self.i}i + {self.j}j + {self.k}k")    


a=twoDVector(1,3)
a.show()

b=threeDVector(2,4,5)
b.show()