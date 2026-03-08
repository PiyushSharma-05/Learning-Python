f=open("poems.txt")
data=f.read()
print(data)
print("\n")
if("twinkle" in data.lower()):
    print("Twinkle is present in the poem")
else:
    print("not present")    
f.close()