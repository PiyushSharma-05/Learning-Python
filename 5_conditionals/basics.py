age=int(input("Enter your age: "))
if(age>100):
    print("Not possible in INDIA")
elif(age>=18):
    print("You are above the age of consent")
    print("definitely it's good for you")
elif(age<0):
    print("You are entrying an invalid age that is negative")
elif(age==0):
    print("You are entrying an invalid age that is zero")
else:
    print("You are below the age of consent")   