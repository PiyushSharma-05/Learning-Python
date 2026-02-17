print( 1+2 , "Hello" + "World") #function overloading

#function overidding
class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")        

t1 = Teacher()
t1.get_designation()

#Duck Typing
class Teacher:
    def get_designation(self):
        print("Designation = Teacher")

class Accountant:
    def get_designation(self):
        print("Designation = Accountant")        

t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()