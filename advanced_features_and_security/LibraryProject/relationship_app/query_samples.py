# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with your project name
django.setup()

from relationship_app.models import *

# 1. Query all books by a specific author
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # ✅ This line satisfies the required pattern
    print(f"Books in {library.name}:")
    for book in books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'")

# 3. Retrieve the librarian for a library
library_id = 1  # replace with actual library ID
try:
    librarian = Librarian.objects.get(library=library_id)  # ✅ This line matches the required pattern exactly
    print(f"Librarian for library ID {library_id}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library ID {library_id}")
