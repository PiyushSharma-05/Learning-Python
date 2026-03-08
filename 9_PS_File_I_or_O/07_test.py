

with open("log.txt") as f:
    # content=f.read()
    # lines=content.split('.')
    lines=f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes python is present at line no.: {lineno}")
        break
    lineno += 1
else:
    print("No , python is not present")    