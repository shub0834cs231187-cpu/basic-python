# Multilevel Inheritance Example
class PrimarySchool:
    def show_10th(self):
        print("My 10th percentage is 80")

class HigherSchool(PrimarySchool):  # inherits PrimarySchool
    def show_12th(self):
        print("My 12th percentage is 75")

class MyCollege(HigherSchool):  # inherits HigherSchool
    def show_cgpa(self):
        print("My CGPA is 7.5")

obj = MyCollege()
obj.show_10th()
obj.show_12th()
obj.show_cgpa()
