class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split(',')
        return cls(name.strip(), int(age.strip()))

p = Person.from_string("Alice, 30")
print(p.name, p.age)   # Alice 30
