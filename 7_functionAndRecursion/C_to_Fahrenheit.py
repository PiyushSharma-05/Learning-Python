
def conversion(c):

    return (9*c/5)+32

c=float(input("Enter temperature in Celsius: "))
f=conversion(c)

# print(f"conversion of {c} degree celsius to fahhrenheit is: {conversion(c)}")
print(f"{round(f,2)} °F")