
from functools import reduce

#Map
nums = [1,2,3,4]
squares =  list(map(lambda x: x**2, nums))
print(squares)

#Filters
f = list(filter(lambda x: x % 2 == 0, nums))
print(f)

#Reduce
r = reduce(lambda x, y: x * y, nums)
print(r)

emails = ["ABHAY@gmail.com","mishra@DATA.in","Tiwari@map.com"]
cleaned = list(map(lambda e:e.strip().lower(),emails))
print(cleaned)

emails = ["ABHAY@gmail.com","mishra@DATA.in","Tiwari@map.com","Hours","bad"]
valid = list(filter(lambda e: "@" in e, emails))
print(valid)
# from functools import reduce
# transactions = [100,-40,90,-50]
# balanace = reduce(lambda acc, t: acc + t, transactions,0)
# print(balanace)