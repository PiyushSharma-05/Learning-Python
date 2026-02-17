class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n
    def __sub__(self,num):
        return self.n-num.n
    def __mul__(self,num):
        return self.n*num.n

a=number(3)
b=number(2)

print(a+b)
print(a-b)
print(a*b)