# class MyClass:
#     def __init__(self,name,age=25):
#         self.name = name   
#         self.age = age     #Instance Variable

#     def display_info(self):
#         print(f"The name of student is {self.name} and age is {self.age}.")

# obj = MyClass("Raj",23)
# obj.display_info()

# obj2 = MyClass("Ram")
# obj2.display_info()


#Class Method
class Config:
    timeout = 30   #Class Variable

c1 = Config()
c2 = Config()
print(c1.timeout,c2.timeout)