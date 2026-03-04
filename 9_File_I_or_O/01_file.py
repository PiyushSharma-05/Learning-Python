# f = open("file.txt","r")
f = open("file.txt")

# data = f.read()
data = f.readline()
print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()