class Student:
    def _init_(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value

s = Student(20)
s.age =22
print(s.age)