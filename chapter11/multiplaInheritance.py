class Employee:
    company ="ITC"
    def show(self):
        print(f"The name is {self.company} ")

class Coder:
    language = "python"
    code = "java"
    def printLanguage(self):
        print(f"your language is {self.language}")


class Programmer(Employee, Coder):
    company ="ITC INFOTEXH"
    def showlanguage(self):
        print(f"The language is {self.code}")





a= Employee()
b=Programmer()

b.show()
b.showlanguage()
b.printLanguage()