# abstraction and encapsulation

class library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrowed_book):
        if borrowed_book in self.books:
            print("get your book now")
            self.books.remove(borrowed_book)
        else:
            print("book not available")

    def recieve_book(self, recieved_book):
        print("you have the returned the book")
        self.books.append(recieved_book)


o = library(["c", "c++", "java", "python"])

msg = """
    1. Display Books
    2. Borrow Book
    3. Return Book
    4. Quit
"""

while True:
    print(msg)
    ch = int(input("Enter your choice : "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter the book to borrow : ")
        o.borrow_book(book)
    elif ch==3:
        book = input("Enter the book to return : ")
        o.recieve_book(book)
    elif ch == 4:
        print("Thank you come again")
        quit()
    else:
        print("Invalid choice")
