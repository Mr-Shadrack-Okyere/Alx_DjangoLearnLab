
---

## **4️⃣ `delete.md`**

```markdown
# Delete Book Instance

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
Book.objects.all()
# <QuerySet []>
