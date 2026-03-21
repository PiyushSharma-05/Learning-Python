# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)


dict1= {"Piyush": 99, "Ambika": 91}
dict2= {"Ambika": 95, "Divya": 92}
merge= dict1 | dict2
print(merge)