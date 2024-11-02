class Employee:
    def __init__(self) -> None:
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self) -> None:
        super().__init__()
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self) :
        super().__init__()
        print("Constructor of Manager")
    c=3


# i=Employee()
# print(i.a)
# u=Programmer()
# print(u.a,u.b)
o=Manager()
print(o.a,o.b,o.c)