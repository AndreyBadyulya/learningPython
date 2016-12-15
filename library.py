import yaml

class Book(object):
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return 'Book: name - "{name}", author - {author}, isbn - {isbn}' \
            .format(name = self.name, author = self.author, isbn = self.isbn)


if __name__ == '__main__':
    book = Book('Lazy stories', 'Mark Smith', 1234554321)
    print yaml.dump(book, open('library.yaml', 'w'), default_flow_style=False)