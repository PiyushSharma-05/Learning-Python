word = "donkey"
with open("para_04.txt") as f:
    content=f.read()

contentNew=content.replace(word,"######")

with open("para_04.txt","w") as f:
    f.write(contentNew)


