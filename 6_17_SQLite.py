import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

create_query = '''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
'''

cursor.execute(create_query)
conn.commit()

insert_query = '''
INSERT INTO books  (title, author, year) VALUES (?, ?, ?)
'''

books =  [
    ('Harry Potter', 'J.K. Rowling', 1997),
    ('1984', 'G. Orwell', 1949),
    ('Мастер и Маргарита', 'М.А. Булгаков', 1967),
]

cursor.executemany(insert_query, books)
conn.commit()

cursor.execute(insert_query, ('Преступление и наказание', 'Фёдор Достоевский', 1866))
conn.commit()


select_query = '''
SELECT * FROM books
'''

cursor.execute(select_query)

all_books = cursor.fetchall()

for book in all_books:
    print(book)


delete_query = '''
DELETE FROM books WHERE title = 'Преступление и наказание'
'''

cursor.execute(delete_query)
conn.commit()


update_query = '''
UPDATE books
SET year = ?
WHERE id = ?
'''

cursor.execute(update_query, (1999, 3))
conn.commit()

cursor.execute(select_query)

all_books = cursor.fetchall()

for book in all_books:
    print(book)

cursor.close()
conn.close()
