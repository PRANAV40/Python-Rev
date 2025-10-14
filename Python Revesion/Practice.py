# kilometer = float(input("Enter the Kilometer:"))

# converstion = 0.621371

# miles = kilometer * converstion
# print(f"The total miles in {kilometer} kilometer is ",miles)

# miles = float(input("Enter the miles: "))
# converstion = 1.609
# kilometer = miles * converstion
# print(f"The total kilometer in {miles} miles is ",kilometer)


# import calendar
# year = int(input("Enter the year"))
# month = int(input("Enter the month"))

# cal = calendar.month(year,month)
# print(cal)


# a = 10
# b = 20

# a,b = b,a
# print(a)
# print(b)

# temp = a
# a = b
# b = temp
# print(a)
# print(b)


# num = float(input("Enter the number"))

# if num > 0:
#     print("Positive")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")


# num = int(input("Enter the number"))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("odd number")


# year = int(input("Enter year here"))

# if year % 400 == 0 and year % 100 == 0:
#     print(f"{year} is leep year.")
# elif year % 4 ==  0 and year % 100 != 0:
#     print(f"{year} is leep year.")
# else:
#     print(f"{year} is not a leep year.")



# def isPrime(num):
#     i = 2
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#         return True

# num = int(input())
# ans = isPrime(num)
# print(ans)

#Factorial in Python
# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num-1)
# num = int(input("Enter a number"))
# ans = factorial(num)
# print(ans)

# def fibonacci(nums):
#     if nums < 0:
#         print("Invaild input.......!")
#     elif nums == 0:
#         return 0
#     elif nums == 1:
#         return 1
#     else:
#         return fibonacci(nums-1) + fibonacci(nums-2) 
# num = int(input("Enter a number: "))
# ans = fibonacci(num)
# print(ans)
#Instance variable  and Class Variable in Python
# print("Instance Variable.....................")
# class School:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = School("Anirudh",18)
# s2 = School("Vishal",19)
# s1.age = 24
# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)

# print("Class variable.....................")
# class Student:
#     school = "VMS"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Student("Ani",19)
# s2 = Student("Vishal",20)
# Student.school = "Sarthi"
# print(s1.name,s1.age,s1.school)
# print(s2.name,s2.age,s2.school)


#Instanc, class and Static method in Python

# class School:
#     student = "Vishal"   #class variable 
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1     #instance variable
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):      #Instance method  
#         return (self.m1 + self.m2 + self.m3)/3
#     @classmethod      #Classs method
#     def getStudent(cls):
#         return cls.student
#     @staticmethod       #Static method
#     def info():
#         print("This is a static methon of school class")

# s1 = School(39,41,20)
# print(s1.avg())
# print(School.getStudent())
# s1.info()
# School.info()

#Inner class 
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.lap = self.Laptop()
    
#     def show(self):
#         print(self.name,self.age)
#         self.lap.show()
    
#     class Laptop():
#         def __init__(self):
#             self.brand = "Dell"
#             self.cpu = 'i5'
#             self.ram = 16
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
        
# s1 = Student("Vishal",19)
# s1.show()

# f = open("File.txt","r")
# print(f.readline())

#Selection sort in ascending and descending order
# def selectionSort(nums):
#     n = len(nums)
#     for i in range(n):
#         minpos = i
#         for j in range(i+1,n):
#             if nums[j] > nums[minpos]:
#                 minpos = j
#         nums[minpos],nums[i] = nums[i],nums[minpos]
# nums = [2,5,3,8,6,9,4]
# selectionSort(nums)
# print(nums)
# def selectionSortDesc(nums):
#     n = len(nums)
#     for i in range(n):
#         minpos = i
#         for j in range(i+1,n):
#             if nums[j] > nums[minpos]:
#                 minpos = j
#         nums[minpos],nums[i] = nums[i],nums[minpos]
# nums = [2,5,3,8,6,9,4]
# selectionSortDesc(nums)
# print(nums)

#Bubble sort in ascending and descending order
# def bubbleSort(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n-1-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
# nums = [2,5,3,8,6,9,4]
# bubbleSort(nums)
# print(nums)

# def bubbleSortDesc(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n-1-i):
#             if nums[j] <  nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
# nums = [2,5,3,8,6,9,4]
# bubbleSortDesc(nums)
# print(nums)


#Insertion sort in ascending and descending order
# def insertionSort(nums):
#     n = len(nums)
#     for i in range(n):
#         j = i
#         while j > 0 and nums[j] < nums[j-1]:
#             nums[j],nums[j-1] = nums[j-1],nums[j]
#             j -= 1
# nums = [2,5,3,8,6,9,4]
# insertionSort(nums)
# print(nums)

# def insertionSortDesc(nums):
#     n = len(nums)
#     for i in range(n):
#         j = i
#         while j > 0 and nums[j] > nums[j-1]:
#             nums[j],nums[j-1] = nums[j-1],nums[j]
#             j -= 1
        
# nums = [2,5,3,8,6,9,4]
# insertionSortDesc(nums)
# print(nums)

#Pattern 
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

#Linear Search in Python

# pos = -1
# def linearSearch(lst,n):
#     i = 0
#     while i < len(lst):
#         if lst[i] == n:
#             globals()['pos'] = i
#             return True
#         i += 1
#     return False

# lst = [3,6,2,8,4,9,1]
# n = 1
# if linearSearch(lst,n):
#     print("Found at",pos)
# else:
#     print("Not found")

#Binary search 
# pos = -1
# def binarySearch(lst,n):
#     l = 0
#     u = len(lst)-1
#     while l <= u:
#         mid = (l+u)//2
#         if lst[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if lst[mid] < n:
#                 l = mid + 1
#             else:
#                 u = mid - 1
#     return False

# lst = [3,6,8,9,11,14,17]
# n = 11
# if binarySearch(lst,n):
#     print("Found at",pos+1)
# else:
#     print("Not found")


# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))

#Airthmetic Operation
# sum_result = num1 + num2
# print(sum_result)

# if num2 == 0:
#     print("Division by Zero is not possible")
# else:
#     div_result = num1 / num2
#     print(int(div_result))

#Area of Triangle
# base = int(input("Enter the base "))
# height = int(input("Enter the height "))

# area = 0.5 * base * height
# print("Area of Trianle is", area)

# a,b = 10,3
# temp = a 
# a = b
# b = temp
# print(a,b)


#ASCII Value of Char
# char = str(input("Enter your char:"))
# print(f"The ASCII Code of {char} is ",ord(char))

#Sum of list
# def sum_of_list(num):
#     total = 0
    
#     for element in num:
#         total += element

#     return total

# lst = [3,5,6,9,2]
# result = sum_of_list(lst)
# print(result)

#Sum of Numbers in List
# numbers = [20,34,21,13,5,7]
# sum_of_numbers = 0
# for i in numbers:
#     sum_of_numbers += i
# print(sum_of_numbers)

#Product of List
# numbers = [2,3,4,1,5]
# product_of_numbers = 1
# for i in numbers:
#     product_of_numbers *= i
# print(product_of_numbers)

#Minimum Number from List
# numbers = [20,34,21,13,5,7]
# minimum_number = numbers[0]
# for i in numbers:
#     if i < minimum_number:
#         minimum_number = i
# print(minimum_number)

#maximum number from List
# numbers = [20,34,21,13,5,7]
# maxinum_number =numbers[0]
# for i in numbers:
#     if i > maxinum_number:
#         maxinum_number = i
# print(maxinum_number)

#Even number from list

# numbers = [20,34,21,13,5,7,8,9,12,11,31,23,16]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

#Odd number from list
# numbers = [20,34,21,13,5,7,8,9,12,11,31,23,16]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)
# def find_largest_element(lst):
#     if not lst:
#         return "List is Empaty"

#     largest_num = lst[0]

#     for element in lst:
#         if element > largest_num:
#             largest_num = element
#     return largest_num

# lst = [9,5,6,3,2]
# result = find_largest_element(lst)
# print(result)


# Count occurrences
# def count_occurrences(l,element):
#     count = l.count(element)
#     return count

# lst = [1,2,3,4,5,6,3,2,4,1,4,5,6,2]
# element_to_count = 2

# occurrence = count_occurrences(lst,element_to_count)
# print(occurrence)


#Swap two variable in Python
# a,b  = 10,21

# print("Before Swapping:",a,b)
# # a,b = b,a
# # a = a + b
# # b = a - b
# # a = a - b
# # temp = a
# # a = b
# # b = temp
# print("after Swappng:",a,b)

#Check Number is Even or Odd using Normal and List Comprehension 
# number = int(input("Enter the number:"))
# if number % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")
# number = [2,5,1,8,7,6]
# result = [num for num in number if num % 2 == 0]
# result1 = [num for num in number if num % 2 != 0]
# print("Even List:",result)
# print("Odd List:",result1)

#factorial in Python
def Factorial(num):
    if num <= 1:
        return 1
    else:
        return  num * Factorial(num - 1)

number = int(input("Enter a number that you want to Factorial: "))
result = Factorial(number)
print(f"The Factorial of {number} is",result)