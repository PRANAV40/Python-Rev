class Example:
    class_count = 0

    def __init__(self, name):
        self.name = name
        Example.class_count += 1

    def instance_method(self):
        return f"instance: {self.name}"

    @classmethod
    def get_count(cls):
        return cls.class_count

    @staticmethod
    def greet(msg):
        return f"Hello: {msg}"

e = Example("x")
print(e.instance_method())   # instance: x
print(Example.get_count())   # 1
print(Example.greet("hi"))   # Hello: hi
