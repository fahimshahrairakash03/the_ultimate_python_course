# c/5=(f-32)/9

def f_TO_C(f):
   return 5*((f-32)/9)
  
f=int(input("Enter temperature in f: "))
print(f"{round(f_TO_C(f),2)} Degree Celcius")