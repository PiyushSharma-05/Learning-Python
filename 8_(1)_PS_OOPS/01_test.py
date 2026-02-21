class programmer:
    company="Microsoft"

    def __init__(self,name,salary,language,pincode):
        self.name=name
        self.salary=salary
        self.language=language
        self.pincode=pincode

p1=programmer("Piyush",1300000,"Python",486001)

print(p1.name,p1.company,p1.salary,p1.language,p1.pincode)

p2=programmer("Ambika",1200000,"C++",289002)

print(p2.name,p2.company,p2.salary,p2.language,p2.pincode)