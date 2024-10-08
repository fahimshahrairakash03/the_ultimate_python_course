
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and c>a):
        return c

a=1
b=23
c=3

print(greatest(a,b,c))