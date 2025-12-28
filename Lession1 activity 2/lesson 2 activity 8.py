class library:
    def __init__(self):
        self.books = ["science", "math", "social", "english"]
    def add_book(self, book):
        self.books.append(book)
        print(book,"successfully added")
    def show_books(self):
        if len(self.books)==0:
            print   ("no books available")
        else:
            print("available books")
            for book in self.books:
                print("-", book)
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)1
            print(book,"issuued successfully")
        else:
            print("book unavailable")
    def return_book(self, book):
        self.books.append(book)
        print(book,"successfully returned")
lib = library()
while True:
    print("\n--- library menu---")
    print("1. add book")
    print("2. show book")
    print("3. issue book")
    print("4. return book")
    print("5. exit")
    choice=int(input("Enter a choice:"))
    if choice == 1:
        book = input("enter book name:")
        lib.add_book(book)
    elif choice == 2:
        lib.show_books()
    elif choice == 3:
        book = input("enter book name to issue")
        lib.issue_book(book)
    elif choice == 4:
        book = input("enter the book to return")
        lib.return_book(book)
    elif choice == 5:
        print("exiting the library")
        break
    else:
        print("invalid choice")

