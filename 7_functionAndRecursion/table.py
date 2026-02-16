n=int(input("Enter the number: "))

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i} ")

print(f"Table of {n} is : ")
table(n)