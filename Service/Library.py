from Database import db
class Library:
    def __init__(self):
        db.connect()
        self.cart = []
    def add_book(self, title, author, year):
        if not title or not author:
            print("Title and Author cannot be empty.")
            return
        try:
            year = int(year)
        except ValueError:
            print("Year must be a number.")
            return
        db.execute_query("INSERT INTO books (title, author, year, status) VALUES (?, ?,?, 'available')",(title, author, year))
        print("Book added.")
    def view_books(self):
        books = db.fetch_query("SELECT * FROM books")
        for book in books:
            print(book)
        
    def search_book(self, title):
        if not title:
            print("Title cannot be empty.")
            return
        books = db.fetch_query("SELECT * FROM books WHERE title LIKE ?", ('%' + title +'%',))
        for book in books:
            print(book)
    def delete_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Book ID must be a number.")
            return
        db.execute_query("DELETE FROM books WHERE id=?", (book_id,))
        print("Book deleted.")
    def issue_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Book ID must be a number.")
            return
        status = db.fetch_query("SELECT status FROM books WHERE id=?", (book_id,))
        if status and status[0][0] == 'available':
            db.execute_query("UPDATE books SET status='issued' WHERE id=?", (book_id,))
            print(f"Book {book_id} issued.")
        else:
            print(f"Book {book_id} not available or doesn't exist.")
    def return_book(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Book ID must be a number.")
            return
        db.execute_query("UPDATE books SET status='available' WHERE id=?", (book_id,))
        print("Book returned.")
    def add_to_cart(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Book ID must be a number.")
            return
        status = db.fetch_query("SELECT status FROM books WHERE id=?", (book_id,))
        if status and status[0][0] == 'available':
            if book_id not in self.cart:
                self.cart.append(book_id)
                print(f"Book {book_id} added to cart.")
            else:
                print("Book already in cart.")
        else:
            print("Book not available or doesn't exist.")
    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("Books in cart:")
        for book_id in self.cart:
            book = db.fetch_query("SELECT * FROM books WHERE id=?", (book_id,))
            if book:
                print(book[0])
    def remove_from_cart(self, book_id):
        try:
            book_id = int(book_id)
        except ValueError:
            print("Book ID must be a number.")
            return
        if book_id in self.cart:
            self.cart.remove(book_id)
            print(f"Book {book_id} removed from cart.")
        else:
            print("Book not in cart.")
    def issue_cart_books(self):
        if not self.cart:
            print("Cart is empty.")
            return
        for book_id in self.cart:
            self.issue_book(book_id)
        self.cart.clear()
        print("All cart books issued.")
    def clear_cart(self):
        self.cart.clear()
        print("Cart cleared.")