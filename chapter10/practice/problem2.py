class Calculator:
    def __init__(self,n) -> None:
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The squareRoot is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareRoot()