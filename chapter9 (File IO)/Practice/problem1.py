f = open("poem.txt")
c=f.read()
if("twinkle" in c):
    print("Present in the conten")
else:
     print("Not present in the conten")

f.close()