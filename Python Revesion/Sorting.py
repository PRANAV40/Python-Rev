from logging.config import stopListening
from pstats import SortKey
from tkinter import PIESLICE


nums = [3,6,2,9,4]
print(sorted(nums))


print(sorted(nums,reverse=True))


names = ["Aman","Pradeep","Rahul","Astuti"]
print(sorted(names))

print(sorted(names,key=str.lower))


#Sorting Dict by values 
score = {"Gill":55,"KLR":37,"Jaiswal":173}
sorted_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
print(sorted_score)