
This file consolidates all the commands and their outputs from the individual Markdown files.

```markdown
## Django Model CRUD Operations

This document details the basic Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model within the Django shell.

### Create Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# <Book: 1984>  (Successful creation of the Book instance)

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

# Title: 1984, Author: George Orwell, Publication Year: 1949

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book_updated = Book.objects.get(id=book.id)
print(book_updated.title)

# Nineteen Eighty-Four

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book_id = book.id # Store the ID before deletion for confirmation
book.delete()
print(Book.objects.filter(id=book_id).exists())
print(Book.objects.all())

# False
# <QuerySet []>