**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book_updated = Book.objects.get(id=book.id)
print(book_updated.title)

# Nineteen Eighty-Four
