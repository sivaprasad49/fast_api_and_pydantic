from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


books = [
    Book(1, 'Think Python', 'Allen', 'Programming book', 4),
    Book(2, 'Think C', 'Allen', 'Programming book', 3),
    Book(3, 'Statistics', 'Allen', 'Maths', 3),
    Book(4, 'Business Communication', 'Allen', 'Language', 4)
]


@app.get("/books")
async def read_all_books():
    return books
