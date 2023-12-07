class Book:
    def __init__(self, book_id=None, title=None, author=None, **kwargs):
        # Initialize book attributes
        self.book_id = book_id
        self.title = title
        self.author = author

        # If any additional keyword arguments are provided, set them as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        # Convert the Book instance to a dictionary
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author
        }

    @classmethod
    def from_dict(cls, data):
        # Create a Book instance from a dictionary
        return cls(**data)

    def __str__(self):
        # String representation of the book for printing
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}"
