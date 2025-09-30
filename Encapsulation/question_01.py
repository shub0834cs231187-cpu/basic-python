class Student:
    def _init_(self, name):
        self.__name = name   # private

    def get_name(self):
        return self.__name

s = Student("Alice")
print(s.get_name())