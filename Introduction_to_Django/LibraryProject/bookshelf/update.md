
---

## **3️⃣ `update.md`**

```markdown
# Update Book Title

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
Book.objects.all()
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
