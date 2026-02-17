class employee:
    company="ITC"
    def show(self):
        print(f"Name is {self.name} and salary is {self.salary}")

class coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all the languages my favourite language is {self.language}")

class programmer(employee , coder):
    company="ITCForce"
    def showLanguage(self):
        print(f"The name is {self.name} and she is good at {self.language} Language")

a=employee()
b=coder()
c=programmer()
c.name="Ambika"
c.salary=100000
c.show()
c.showLanguage()
c.printLanguage()