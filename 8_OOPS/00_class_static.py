class Employee:
    language="Python"  #these are class attibutes
    salary=1200000

    def getInfo(self):
        print(f"salary is: {self.salary} , language is: {self.language}")

    def greet1(self):
        print(f"Good Morning From {self.name}")    
    
    @staticmethod  # marks as static
    def greet2():
        print(f"Good Morning ")     

e1=Employee()
e1.name="Piyush"

e2=Employee()
e2.name="Ambika"  # these are instance attributes 
e2.language="C++"  # instance attributes takes priority over class attributes


# print(e1.name,e1.language,e1.salary)
# print(e2.name,e2.language,e2.salary)

e1.getInfo()  # = Employee.getInfo(e1)
e2.greet1()
e2.getInfo()
e1.greet2()
 