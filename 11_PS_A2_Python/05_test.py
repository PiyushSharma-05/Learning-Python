from functools import reduce

def max(a,b):
    if(a>b):
        return a
    return b

l= [2,5,89,23,100,90,341,321,351,352]

a=reduce(max, l)

print(a)