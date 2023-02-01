class Book:
    def __init__(self, title, author, genre, read_time, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.read_time = read_time
        self.id = id