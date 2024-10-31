with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Pyhton is presen")
else:
    print("Pyhton is not presen")
