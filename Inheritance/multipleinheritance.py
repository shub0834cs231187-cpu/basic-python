# Multiple Inheritance Example
class PrimarySchool:
    def show_10th(self):
        print("My 10th percentage is 80")

class HigherSchool:
    def show_12th(self):
        print("My 12th percentage is 75")

class MyCollege:
    def show_cgpa(self):
        print("My CGPA is 7.5")

class Company(PrimarySchool, HigherSchool, MyCollege):  # Multiple inheritance
    def show_package(self):
        print("My package is 10 LPA")

object = Company()
object.show_10th()
object.show_12th()
object.show_cgpa()
object.show_package()
