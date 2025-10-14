class A:
    def __init__(self):
        print("Class A initializer!")

class B(A):
    pass

class C(A):
    def __init__(self):
        print("Class C initializer")

class D(A):
    def __init__(self):
        super().__init__()
        print("Class D initializer")


d = D()

class Config:
    DB_HOST = "localhost"
    DB_PORT = 5432

class ProdConfir(Config):
    DB_HOST = "prod-db.example.com"
