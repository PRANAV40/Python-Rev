from abc import ABC, abstractmethod

class Vehicle(ABC):  # Inheriting from ABC makes it abstract
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# This will cause an error if we try to instantiate Vehicle
# v = Vehicle()  # ❌ TypeError: Can't instantiate abstract class

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

# ✅ Works fine because Car implemented all abstract methods
my_car = Car()
my_car.start()
my_car.stop()
