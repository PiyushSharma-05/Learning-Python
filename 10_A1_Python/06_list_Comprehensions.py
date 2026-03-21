l= [2,4,5,3,2,7,8,11,14,15,4,5]

# squareList= []
# for i in l:
#     squareList.append(i*i)

# print(squareList)    

#This can be done easily by using list comprehensions

# squareList=[i*i for i in l if i%2 !=0]

# print(squareList) 

# l2 = [-2,-2,3,4,-1,7,-9]

# nums = [0 if val<0 else val for val in l2]
# print(nums)

# words = ["Piyush", "Ambika", "Divya"]

# WORDS = [val.upper() for val in words]

# print(WORDS)

l2 = [34,45,12,9,7,3,12,89,2,67,78]

LG = [val for val in l2 if val>30]
print(LG)