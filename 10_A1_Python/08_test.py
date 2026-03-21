import json

data = {
    "Jabalpur" : 10000,
    "Rewa" : 20000,
    "Agra" : 30000
}

file = "cities.json"

with open(file, "w") as f:
    json.dump(data, f, indent=4)

with open(file, "r") as f:
    material = json.load(f)
    print(material)

new_city = input("Enter a new city: ")
pop_city = input("Enter population of that city: ")

material[new_city] = pop_city

with open(file, "w") as f:
    json.dump(material, f, indent=4)

print(material)