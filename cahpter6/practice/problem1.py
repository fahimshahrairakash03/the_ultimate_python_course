a1= int(input("Enter number 1: "))
a2= int(input("Enter number 2: "))
a3= int(input("Enter number 3: "))
a4= int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest: ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest: ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest: ",a3)
elif(a4>a1 and a4>a3 and a4>a2):
    print("Greatest: ",a4)