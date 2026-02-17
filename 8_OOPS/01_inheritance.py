class employee:
    company="ITC"
    def show(self):
        print(f"Name is {self.name} and salary is {self.salary}")

class programmer(employee):
    company="ITC ITCForce"
    def showLanguage(self):
        print(f"The name is {self.name} and she is good at {self.language} Language")


e1=employee()
e1.name="Piyush"
e1.salary=130000
print(f"{e1.company}")
e1.show()

p1=programmer()
p1.name="Ambika"
p1.language="Python"
print(f"{p1.company}")
p1.show
p1.showLanguage()