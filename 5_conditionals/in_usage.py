p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

messege=input("Enter your messege: ")

if((p1 in messege) or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("This messege is a spam")
else:
    print("All is well with this messege")    