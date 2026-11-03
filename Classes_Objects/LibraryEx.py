
# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program is stopped!
class Library:
    def __init__(self):
        self.No_of_books=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.No_books=len(self.books)

    def showDetails(self):
        print(f"The num of books are {self.No_books} named {self.books}")

l1=Library()
l1.addbook("Harry Potter")
l1.addbook("The art of not giving a fuck")
l1.showDetails()
