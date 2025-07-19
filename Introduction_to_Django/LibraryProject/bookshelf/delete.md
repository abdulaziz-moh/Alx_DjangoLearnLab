**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book_id = book.id # Store the ID before deletion for confirmation
book.delete()
print(Book.objects.filter(id=book_id).exists())
print(Book.objects.all())

# False
# <QuerySet []>