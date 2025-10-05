#Conditional Statements

# if number_of_impressions >= 5000000:
#     print("you are eligible for monetization")


#Real Life secenrios are different
reputation_score = 75

if reputation_score >= 90:
    boost = "maximum"
elif reputation_score >= 75:
    boost = "medium"
else:
    boost= "minimum"

print(boost)


#Ternary Operator
print("Ternary Operator")
age = 21
status = "Adults" if age >= 18 else "Minor"
print(status)

#Match case
from http import HTTPStatus

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

#Example: With Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Pranav", 24)

match p:
    case Person(name="Pranav", age=24):
        print("Exact match!")
    case Person(name=n, age=a):
        print(f"Person named {n} aged {a}")
