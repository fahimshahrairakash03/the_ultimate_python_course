class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property 
    def name(self):
         return self.fname
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e= Employee()
e.a =45
e.name = "Akash Shahriar"
print(e.fname,e.lname)
e.show()