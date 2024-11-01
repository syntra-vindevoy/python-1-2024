import uuid

class Item:
    def __init__ (self, title, author, price, page_count):
        self.id = uuid.uuid4 ()
        self.title = title
        self.author = author
        self.price = price
        self.page_count = page_count

    def __str__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} "

    def __repr__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} "

    def __eq__ (self, other):
        return self.id == other.id

    def __hash__ (self):
        return hash (self.id)


class Book (Item):
    def __init__ (self, title, author, price, page_count, book_genre):
        super ().__init__ (title, author, price, page_count)
        self.book_genre = book_genre

    def __str__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} {self.book_genre}"

    def __repr__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} {self.book_genre}"


class Comic (Item):
    def __init__ (self, title, author, price, page_count, comic_genre):
        super ().__init__ (title, author, price, page_count)
        self.comic_genre = comic_genre

    def __str__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} {self.comic_genre}"

    def __repr__ (self):
        return f"{self.title} by {self.author} costs {self.price}  {self.page_count} {self.comic_genre}"


class BookStore[T:(Book, Comic)]:
    def __init__ (self):
        self.books: set[T] = set[T] ()

    def add_item (self, book: T):
        if isinstance (book, (Book, Comic)):
            if book not in self.books:
                self.books.add (book)
            else:
                raise Exception (f"Book already exists {book.id}")
        else:
            raise TypeError ("Not a valid book or comic")

    def get_total_price (self):
        total_price = 0
        book: T
        for book in self.books:
            total_price += book.price
        return total_price

    def get_all_books (self):
        return self.books

    def get_all_books_type (self, type_item: type) -> int:
        result_types = 0
        book: T
        for book in self.books:
            if isinstance (book, type_item):
                result_types += 1
        return result_types

    def __str__ (self):
        return f"Total Books {len (self.books)} {self.get_total_price ()}"

    def __repr__ (self):
        return f"Total Books {len (self.books)} {self.get_total_price ()}"


if __name__ == '__main__':
    book_store = BookStore[Item] ()
    book_store.add_item (Book (title="supernova", book_genre="Fantasy", author="benoit", price=5.5, page_count=200))
    book_store.add_item (Book (title="supernova2", book_genre="Fantasy", author="benoit", price=5.5, page_count=200))
    book_store.add_item (Book (title="supernova3", book_genre="Fantasy", author="benoit", price=5.5, page_count=200))

    book_store.add_item (
        Comic (title="Comicsupernova4", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200))
    book_store.add_item (
        Comic (title="Comicsupernova5", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200))
    book_store.add_item (
        Comic (title="Comicsupernova6", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200))
    book_store.add_item (
        Comic (title="Comicsupernova7", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200))

    for book in book_store.get_all_books ():
        print (f"{book}")

    a = Comic (title="Comicsupernovatest", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200)
    b = Comic (title="Comicsupernovatest", comic_genre="Fantasy", author="benoit", price=5.5, page_count=200)
    b.id = a.id
    book_store.add_item (a)
    try:
        book_store.add_item (b)
    except Exception as X:
        print (X)

    try:
        book_store.add_item (())
    except Exception as X:
        print (X)

    print (book_store)
    print (book_store.get_all_books_type (Book))
    print (book_store.get_all_books_type (Comic))