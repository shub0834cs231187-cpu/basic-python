#  8. Book — Display Title and Author


class Book:
    def __init__(self, title, author,referencenumber):
        self.title = title
        self.author = author
        self.referencenumber =referencenumber

    def info(self):
        print(f"'{self.title}' by {self.author}"and {self.referencenumber})

book = Book("1984", "premchand",1547856)
book.info()



