from resource import Book

class ResourceManager:
    def __init__(self):
        self.books = []

    def create_resource(self):
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def search_resources(self, criteria):
        matching_books = [book for book in self.books if criteria.lower() in book.title.lower()]
        return matching_books

    def edit_resource(self):
        book_id = int(input("Enter the book ID to edit: "))
        book_to_edit = next((book for book in self.books if book.book_id == book_id), None)

        if book_to_edit:
            new_title = input(f"Enter the new title for book ID {book_id}: ")
            new_author = input(f"Enter the new author for book ID {book_id}: ")

            book_to_edit.title = new_title
            book_to_edit.author = new_author

            print(f"Book with ID {book_id} edited successfully!")
        else:
            print(f"Book with ID {book_id} not found.")

    def delete_resource(self):
        book_id = int(input("Enter the book ID to delete: "))
        book_to_delete = next((book for book in self.books if book.book_id == book_id), None)

        if book_to_delete:
            self.books.remove(book_to_delete)
            print(f"Book with ID {book_id} deleted successfully!")
        else:
            print(f"Book with ID {book_id} not found.")

    def get_all_resources(self):
        return [book.to_dict() for book in self.books]
