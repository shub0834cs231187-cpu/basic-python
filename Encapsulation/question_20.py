class Employee:
    def _init_(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value

