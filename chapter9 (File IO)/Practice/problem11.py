with open ("old.txt") as f:
    content1 = f.read()

with open ("rename.txt","w") as f:
    f.write(content1)