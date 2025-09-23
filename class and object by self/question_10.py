## 10. Dog — Make It Bark


class Dog:
    def __init__(self, name,colour,breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def bark(self):
        print(f"{self.name},{self.colour},{self.breed}")

dog = Dog("Buddy","black","pitbull")
dog.bark()
