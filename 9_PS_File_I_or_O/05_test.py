words = ["donkey","bad","ganda"]
with open("para_05.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#"*len(word))


with open("para_05.txt","w") as f:
    f.write(content)

