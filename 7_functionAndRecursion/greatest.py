def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
  
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 1st number: "))
c=int(input("Enter the 1st number: "))

print(f"Greatest among the 3 is : {greatest(a,b,c)}")