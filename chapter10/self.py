class Employee:
    language= "Python"
    salary= 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
# harry.language = "Java"
harry.getInfo()
# Employee.getInfo(harry)
harry.greet()