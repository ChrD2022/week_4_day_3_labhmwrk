import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("Roald", "Dahl")
author_repository.save(author_1)

book_1 = Book("The Enormous Crocodile", author_1, "Childrens", 2)
book_repository.save(book_1)
book_2 = Book("The Twits", author_1, "Childrens", 3)
book_repository.save(book_2)
book_3 = Book("Matilda", author_1, "Childrens", 6)
book_repository.save(book_3)

pdb.set_trace()