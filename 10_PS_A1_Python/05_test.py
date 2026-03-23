n=int(input("Enter the number for table: "))

Table= [n*i for i in range(1,11)]

print(Table)

# with open("Tables.txt","w") as f:
#     f.write(str(Table))

with open("Tables.txt", "a") as f:
    f.write(f"Table of {n} is: {str(Table)}\n")