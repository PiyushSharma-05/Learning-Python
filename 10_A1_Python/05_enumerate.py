l=[2,4,5,1,3]

# index=0
# for i in l:
#     print(f"The number at index {index} is {i}")
#     index+=1

#This can be easily done by using enumerate function

for index, item in enumerate(l):
     print(f"The number at index {index} is {item}")