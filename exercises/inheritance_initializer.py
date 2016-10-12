class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages
#         self.format = format

# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format):
#         Book.__init__(self, title, publisher, pages)
#         self.format = format


class Ebook(Book):
    def __init__(self, title, publisher, pages, format):
        super().__init__(title, publisher, pages)
        self.format = format
