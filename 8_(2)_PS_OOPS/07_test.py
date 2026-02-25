class Vector:
    def __init__(self,l):
       self.l=l
    def __len__(self):
       return len(self.l) 
    

v1=Vector([2,3,4]) # passed as a list to print length
print(len(v1))