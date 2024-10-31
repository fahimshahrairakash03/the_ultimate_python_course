
with open("./log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Pyhton is present. Line no: {line}")
        break
    lineno +=1

else:
    print("No python is present")
