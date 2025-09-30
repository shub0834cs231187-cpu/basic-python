# Single Inheritance Example
class PrimarySchool:
    def show_10th(self):
        print("My 10th percentage is 80")

class HigherSchool(PrimarySchool):  # Inheriting from PrimarySchool
    def show_12th(self):
        print("My 12th percentage is 75")

object = HigherSchool()
object.show_10th()
object.show_12th()
