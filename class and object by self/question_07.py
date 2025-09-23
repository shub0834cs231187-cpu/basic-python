# 7. Counter — Track Count

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print("Count:", self.count)

c = Counter()
c.increment()
c.increment()
c.display()
