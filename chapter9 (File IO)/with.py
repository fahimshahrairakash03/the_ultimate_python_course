f= open("file.txt")
print(f.read())
f.close()

#the same can be done with using hte with statement:

with open("file.txt") as f:
    print(f.read())

#you don't have to explicitly close the file