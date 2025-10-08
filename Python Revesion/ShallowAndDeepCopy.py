import copy
from tkinter import PIESLICE
a = [10,21,34]
b = copy.copy(a)

b[0] = 40
print(b)
print(a)


a = [[23,45],[26,41]]
b = copy.copy(a)
b[0][0] = 99
print(a)
