class Employee:
    company ="ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    
# class Programmer:
#     company ="ITC INFOTEXH"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")

#     def showLangiage(self):
#         print(f"The name is {self.name} and language is {self.language}")

class Programmer(Employee):
    company ="ITC INFOTEXH"
    def showlanguage(self):
        print(f"The language is {self.language}")





a= Employee()
b=Programmer()
print(a.company,b.company)
