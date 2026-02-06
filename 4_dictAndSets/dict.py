a={}  # for a empty Dict
marks={
    "Piyush":99,
    "Ambika":97,
    "Rahul":80,
    "Divya":77
}

print(marks)
print(marks.keys())
print(marks.items())
print(marks.values())
marks.update({"Rahul":87})
marks.update({"Divya":71})
marks.update({"Karan":34})
print(marks)
print(marks.keys())
print(marks.values())
print(marks.items())

print(marks["Piyush"])
print(marks["Ambika"])
print(marks.get("Karan")) #returns none
print(marks["Karan"]) #returns error