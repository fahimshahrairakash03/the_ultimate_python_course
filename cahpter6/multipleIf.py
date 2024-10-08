a= int(input("Enter age: "))
if(a%2==0):
    print("a is even")
if(a>=18):
    print("You are above the age on consent")
elif(a<0):
    print("you are entering in an invalid age")
elif(a==0):
    print("you are entering in 0 which is not an age")
else:
    print("You are below the age on consent")

print("End of program")