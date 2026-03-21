try:
    a=int(input("Enter a NUmber: "))
    print(a)

except Exception as e:
    print(e)
finally:
    print("End of program")

print("Thank You")    

try:
    p=int(input("Enter the first number: "))
    q=int(input("Enter the second number: "))

except ValueError:
    print("invalid number !")
else:    
    if(q==0):
        raise ZeroDivisionError("Hey we can't divide a number by zero!")
    else:
        print("The result of p/q is:",p/q)
   