# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=int(input("Enter 3rd number: "))
# d=int(input("Enter 4th number: "))

# if(a>b and a>c and a>d):
#     print(f"{a} is the greatest among all!")
# elif(b>a and b>c and b>d):
#     print(f"{b} is the greatest among all!")
# elif(c>a and c>b and c>d):
#     print(f"{c} is the greatest among all!")
# else:
#     print(f"{d} is the greatest among all!")

# m1=int(input("Enter marks of subject 1: "))
# m2=int(input("Enter marks of subject 2: "))
# m3=int(input("Enter marks of subject 3: "))

# marks=(m1+m2+m3)/3


# if(marks<40 or m1<33 or m2<33 or m3<33 ):
#     print(f"You got failed! and got {marks} percentage")
#     print("Try again next year")
# else:
#     print(f"Congrats! you have been passed and got {marks} percentage")

# username=input("Enter your username: ")
# if(len(username)<10):
#     print("Entered username contains less than 10 characters!")
# else:
#     print("All is well this username it's acceptable")    

# l=["Piyush","Ambika","Rahul","Karan","Divya","Shareen","Aman","Arjun","Krishak"]

# name=input("Enter your name: ")

# if(name in l):
#     print("List contains this name!")
# else:
#     print("List doesn't contains this name!")    

marks=int(input("Enter marks of the subject: "))





if(marks<=100 and marks>90):
    grade="Ex"
elif(marks<=90 and marks>80):
    grade="A"
elif(marks<=80 and marks>70):
    grade="B"
elif(marks<=70 and marks>60):
    grade="C"
elif(marks<=60 and marks>50):
    grade="D"
else:
    grade="Fail !"                   


print(f"Grades: {grade}")