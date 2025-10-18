##used to define common methods for a group of related objects. they cannot be instantiated directly.
from abc import ABC, abstractmethod
class veichle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class car(veichle):
    def start_engine(self):
        return "Car engine started"
class bike(veichle):
        def start_engine(self):
            return "Bike engine started"
car1=car()
bike1=bike()
print(car1.start_engine())
print(bike1.start_engine())