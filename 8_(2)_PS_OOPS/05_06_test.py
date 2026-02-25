class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self,v2):
        return Vector(self.i+v2.i,self.j+v2.j,self.k+v2.k)
    
    def __mul__(self,v2):
        result=(self.i*v2.i + self.j*v2.j + self.k*v2.k)
        return result
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1=Vector(2,3,4)
v2=Vector(1,4,2)
print("Addition:",v1+v2)
print("Product:",v1*v2)