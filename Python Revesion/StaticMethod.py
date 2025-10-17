class MathHelpers:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelpers.add(2, 3))    # 5
m = MathHelpers()
print(m.add(4, 5))              # 9
