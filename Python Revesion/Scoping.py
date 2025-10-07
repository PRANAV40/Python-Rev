#Local scoping refers to variables defined within a function

#These variables are only accessible within the function and are not visible outside it
# def my_function():
#     x = 10
#     print(x)

# my_function()


#Enclosing scoping refers to variables defined in the enclosing function

#This applies to nested functions, where variables defined in the outer function can be accessed by the inner function
# def outer_function():
#     x = 10
#     def inner_function():
#         print(x)
#     inner_function()
# outer_function()


#Global scoping refers to variables defined at the top level of a module

#These variables are accessible from any part of the module

# x = 10
# def my_function():
#     print(x)
# my_function()
# print(x)