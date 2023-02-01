from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author, genre, read_time) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre, book.read_time]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author'])
        book = Book(row['title'], author, row['genre'], row['read_time'], row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['genre'], result['read_time'], result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, book_id, genre, read_time) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.read_time, book.id]
    run_sql(sql, values)
