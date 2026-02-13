n=int(input("Enter the number: "))
for i in range(1,11):
    if(i==7):
        continue
    print(f"{n} * {i} = {n*i}")

n=int(input("Enter the number: "))
for i in range(1,11):
    if(i==7):
      break
    print(f"{n} * {i} = {n*i}")