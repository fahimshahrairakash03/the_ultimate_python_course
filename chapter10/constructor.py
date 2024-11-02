class Employee:
    language= "Python"
    salary= 120000

    def __init__(self,name,salary,language) -> None: #dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee("Harry",130000,"Javascript")
# harry.name="Harry"
print(harry.name,harry.salary,harry.language)