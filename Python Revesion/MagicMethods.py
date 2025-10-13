class Point:
    def __init__(self, x, y):    #Constructor of the class
        self.x = x    #Instance Variable
        self.y = y

    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Length (distance from origin)
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)


# Using the class
p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)            # Calls __str__ → Point(3, 4)
print(p1 + p2)       # Calls __add__ → Point(4, 6)
print(len(p1))       # Calls __len__ → 5
