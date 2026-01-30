class Book:
    def __init__(self,book_name,author,available=True):
        self.book_name=book_name
        self.author=author
        self.available=available
        
    def check_out(self):
        if self.available:
            self.available=False
            print(f"'{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"'{self.book_name}' by {self.author} is currently unavailable.")

    def return_book(self):
        
        if not self.available:
            self.available = True
            print(f"'{self.book_name}' by {self.author} has been returned and is now available.")
        else:
            print(f"'{self.book_name}' by {self.author} was not checked out.")

    def display_status(self):
        
        status = "Available" if self.available else "Checked out"
        print(f"'{self.book_name}' by {self.author} is {status}.")

# Example usage:
library_books = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee")
    
]

while True:
    print("\nLibrary Menu:\n1. Display all books\n2. Check out a book\n3. Return a book\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book in library_books:
                book.display_status()

    elif choice == "2":
        book_name = input("Enter the name of the book to check out: ")
        for book in library_books:
            if book.book_name.lower() == book_name.lower():
                book.check_out()
                break
        else:
            print("Book not found in the library.")

    elif choice == "3":
        book_name = input("Enter the name of the book to return: ")
        for book in library_books:
            if book.book_name.lower() == book_name.lower():
                book.return_book()
                break
        else:
            print("Book not found in the library.")

    elif choice == "4":
        print("Exiting the library system. Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")