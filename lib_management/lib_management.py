import pandas as pd

class Book:
  def __init__(self, title, author, available=True):
    # The book's title
    self.title = title
    # The book's author
    self.author = author
    # Availability of the book
    self.available = available

  def __str__(self):
    return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Not Available'}"


book1 = Book("1984", "George Orwell")



# Empty datafram to hold books
books_df = pd.DataFrame(columns=['Title', 'Author', 'Available'])


def add_book_to_df(book):
  index = len(books_df)
  books_df.loc[index] = [book.title, book.author, book.available]

add_book_to_df(book1)
print(books_df)

# find all available books
available_books = books_df[books_df['Available'] == True]
print(available_books)


