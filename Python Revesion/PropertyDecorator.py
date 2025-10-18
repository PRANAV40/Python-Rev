class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullName(self):
        return self.fname + " " + self.lname

p = Person("Jai","deep")
print(p.fullName)