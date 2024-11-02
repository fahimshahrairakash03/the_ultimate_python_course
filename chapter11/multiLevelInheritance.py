class Employee:
    def __init__(self) -> None:
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3


i=Employee()
print(i.a)
u=Programmer()
print(u.a,u.b)
o=Manager()
print(o.a,o.b,o.c)