#Factorial
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num-1)

# print("Factorial of number is",factorial(5))

# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]

# print(is_palindrome("Madam"))

# def largest_number(numbers):
#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest

# print(largest_number([45,7,97,23,12,32,44]))

# def count_vowels(s):
#     vowels = "AEIOUaeiou"
#     return sum(1 for char in s if char in vowels)

# print("Count Vowels",count_vowels("Python Language"))

# def avg(num):
#     return sum(num) / len(num)

# print(avg([12,14,16,18,22]))

#Positonal Argument
# def greet(name:str,age:int):
#     print(f"Name is {name} and the age is {age}")

# greet("Pranav",25)

#Keyword Argument
# greet(age=25,name="Amit")

#Defult Argument
# def power(base:int,exp:int=2):
#     return base ** exp

# print(power(3))
# print(power(3,3))