class employee():
    salary=1300000
    language="Python"

    def __init__(self,name):  #automatically get called over object creation
        print("I am creating an object")
        self.name=name
        

e1=employee("Piyush")
print(e1.name,e1.salary,e1.language)

e2=employee("Ambika")

print(e2.name,e2.salary,e2.language)
