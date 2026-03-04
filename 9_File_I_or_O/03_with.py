# f=open("myfile.txt")
# print(f.read())
# f.close()

#this can also be written as -
with open("myfile.txt") as f:
    print(f.read())
#you dont have to explicitly close file    