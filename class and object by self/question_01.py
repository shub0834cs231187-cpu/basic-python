# Person Class — Display Name and Age

class Person:
    def __init__(self, name, age ,email,contactnumber):
        self.name = name
        self.age = age
        self.email= email
        self.contactnumber= contactnumber

    def display(self):
        print(f"Name: {self.name}, Age: {self.age},email:{self.email},contactnumber:{self.contactnumber}")

p = Person("shubham", 25,"shub@gmail.com",8720804613)
p.display()

