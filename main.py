from Authentication.Auth import Auth
from Service.Library import Library
import getpass
auth = Auth()
lib = Library()
def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Add Book to Cart")
        print("8. View Cart")
        print("9. Remove Book from Cart")
        print("10. Issue All Cart Books")
        print("11. Clear Cart")
        print("12. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            lib.add_book(title, author, year)
        elif choice == '2':
            lib.view_books()
        elif choice == '3':
            title = input("Title to search: ")
            lib.search_book(title)
        elif choice == '4':
            book_id = input("Book ID: ")
            lib.delete_book(book_id)
        elif choice == '5':
            book_id = input("Book ID: ")
            lib.issue_book(book_id)
        elif choice == '6':
            book_id = input("Book ID: ")
            lib.return_book(book_id)
        elif choice == '7':
            book_id = input("Book ID: ")
            lib.add_to_cart(book_id)
        elif choice == '8':
            lib.view_cart()
        elif choice == '9':
            book_id = input("Book ID: ")
            lib.remove_from_cart(book_id)
        elif choice == '10':
            lib.issue_cart_books()
        elif choice == '11':
            lib.clear_cart()
        elif choice == '12':
            break
        else:
            print("Invalid choice or option.")
def main():
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        option = input("Enter option: ")
        if option == '1':
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            if auth.login(username, password):
                library_menu()
        elif option == '2':
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            auth.signup(username, password)
        elif option == '3':
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()