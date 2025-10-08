#Without Context Manager
f = open("abc.txt","r")
data = f.read()
f.close()


#Using Context Manager
with open("abc.txt","r") as f:
    data = f.read()