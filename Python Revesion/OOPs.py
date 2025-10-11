class EmployeeToDemoInit():
    BASE_PAY = 2500    #Class attrbute or Static

    def __init__(self,name,departmrnt):
        self.name = name      #Instance Attribute
        self.depeartment = departmrnt

    
    def calculate_employee_bonus(self):
        return EmployeeToDemoInit.BASE_PAY + EmployeeToDemoInit.BASE_PAY * .3    


object1 = EmployeeToDemoInit("Amit","Data")
print(object1.name)
print(object1.depeartment)
print(object1.calculate_employee_bonus())
object2 = EmployeeToDemoInit("Aniket","DevOps")
print(object2.name)
print(object2.depeartment)
print(object2.calculate_employee_bonus())
