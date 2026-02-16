def rem(l): #remove the word
    for item in l:
        l.remove("an")

        return l    

def stripAndRemove(l,word):#strips and removes the word
    n=[]
    for item in l:
        if (item!=word):
            n.append(item.strip(word))
    return n        

l=["Piyush","Aman","Shubham","Anamika","an","vikram","Ambika","anuj","vanar"]
print(rem(l))

print(stripAndRemove(l,"an"))