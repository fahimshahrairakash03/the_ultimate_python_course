class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin) -> None:
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Fhaim",12000,242323)
print(p.name,p.salary,p.pin)
r = Programmer("Rohan",15000,24665)
print(r.name,r.salary,r.pin)