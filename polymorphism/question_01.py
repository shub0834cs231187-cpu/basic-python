class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())
