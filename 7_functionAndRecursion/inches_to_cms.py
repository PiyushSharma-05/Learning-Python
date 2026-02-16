n=int(input("Enter measurement in inches: "))

def inchesToCms(n):
  value= n*2.54
  return value

print(f"cm conversion of {n} inches is: {inchesToCms(n)}")