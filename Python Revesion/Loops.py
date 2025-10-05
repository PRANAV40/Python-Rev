#Loops

for i in range(5):
    print(i)

names = ["Pranav","Nobita","Ayush"]
for name in names:
    print("Hello",name)

for ch in "Pranav":
    print(ch, end=" ")

#Break, Countinue and Else
for num in range(5):
    if num == 3:
        break
    if num == 1:
        continue
    print(num)
else:
    print("Loop finished without break")

my_dict = {"username":"pranav40","password":"pranav@30","captacha":"245HA"}
for key, value in my_dict.items():
    print(key,value)

#While loop
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # increase count each time

print("Loop finished!")


#Real-World Example
password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted!")

