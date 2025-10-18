
# def greet():
#     print("Hello, World!")

def decorator_function(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

# decorated = decorator_function(greet)
# decorated()

@decorator_function
def greet():
    print("Hello, World!")

greet()
