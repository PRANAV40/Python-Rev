# class User:
#     def __init__(self,name):
#         self.name = name
#         print(f"Self id:{id(self)} name:{id(name)}")

# u1 = User("Ajay")
# u2 = User("Alok")

# print("u1 id:",id(u1))
# print("u2 id:",id(u2))


class User:
    users = 0
    def __init__(self,name):
        self.name = name
        User.users += 1
        print(f"Self is {self.name}, cls is User (total users: {User.users})")

    @classmethod
    def total_users(cls):
        return cls.users

u1 = User("Ajay")
u2 = User("Alok")

print("Total users:", User.total_users())
