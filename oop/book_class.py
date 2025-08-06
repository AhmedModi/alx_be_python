# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: User-friendly format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Used for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
