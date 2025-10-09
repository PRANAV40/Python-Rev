from collections import Counter
# logs = ["error","info","error","debug","info","error"]

# c = Counter(logs)
# print(c)

# print(c.most_common(1))


# text = "python is fun and python is powerful"
# words = text.split()

# c = Counter(words)
# print(c.most_common(2))


a = Counter("Hello")
b = Counter("World")

print(a + b)
print(a - b)