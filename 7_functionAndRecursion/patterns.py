'''
***
**
*
'''
n=int(input("Enter the number: "))

def patterns(n): #without recursion
    for i in range(0,n):
        print("*"* (n-i))


def pattern(n):
    if(n==0):
        return
    print(f"*"* n)
    pattern(n-1)

print("pattern is - ")
pattern(n)