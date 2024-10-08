n=int(input("Enter a number: "))

for i in range(1,n+1):
    print(f"{n} X {(n+1)-i} = {n*((n+1)-i)}")