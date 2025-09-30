from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        return 50000

class Manager(Employee):
    def salary(self):
        return 80000

print(Developer().salary())
print(Manager().salary())
