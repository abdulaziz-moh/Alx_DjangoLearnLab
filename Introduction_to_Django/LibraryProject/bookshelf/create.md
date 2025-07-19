**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Output:

# <Book: 1984>  (Successful creation of the Book instance)