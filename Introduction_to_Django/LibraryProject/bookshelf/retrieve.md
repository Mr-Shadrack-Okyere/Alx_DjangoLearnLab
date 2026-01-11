# Retrieve Book Instance

```python
from bookshelf.models import Book

# Retrieve the book instance using get()
book = Book.objects.get(title="1984")
book
# <Book: 1984 by George Orwell (1949)>
