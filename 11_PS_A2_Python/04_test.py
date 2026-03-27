l= [2,5,120,2385,458,23780,1245,29]

def divisible(n):
    if(n%5==0):
        return True
    return False

a= list(filter(divisible, l))
print(a)