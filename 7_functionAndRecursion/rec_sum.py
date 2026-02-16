n=int(input("Enter the number: "))

def recSum(n):
    if(n==1):
      return 1
    return n + recSum(n-1) 

print(f"recursive sum of first {n} natural numbers is: {recSum(n)}")