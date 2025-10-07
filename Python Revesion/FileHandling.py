#File Handling in Python

# f = open("abc.txt","r") 
# print(f.read)
# f.close()

# with open("abc.txt","r") as f:
#     content = f.read
# print("Done, file is close Automaticaly")

f1 = open("abc.txt",'w')
f1.write("Hello, I am Pranav Mishra")
f2 = open("abc.txt",'r')
content = f2.read()
print(content)
f2.close()

# import os
# print(os.getcwd())
# print(os.path.join("data","abc.txt"))

