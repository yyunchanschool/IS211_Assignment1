class Book():
    author = ""
    title = ""
    def __init__ (self, author, title):
        self.author = author
        self.title = title
    def display (self):
        print (str(self.title + ", written by " + self.author))

object1 = Book ("John Steinbeck", "Of Mice and Men")
object2 = Book ("Harper Lee", "To Kill a Mockingbird")

object1.display()
object2.display()