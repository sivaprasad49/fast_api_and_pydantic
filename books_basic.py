from fastapi import FastAPI

app = FastAPI()

books = [{'title':'think python', 'version':1, 'category': 'Engineering', 'language': 'English'}, 
         {'title':'think C', 'version':1, 'category': 'Engineering', 'language': 'Spanish'},
         {'title':'Statistics', 'version':1, 'category': 'Maths', 'language': 'English'},
         {'title':'Business Communication', 'version':1, 'category': 'Language', 'language': 'English'}]
@app.get("/books")
async def read_all_books():
    return books


@app.get("/books/my_book")
async def read_all_books():
    return books[0]

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_book_by_category(category: str):
    books_to_return = []
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book.get('title'))
    return books_to_return

@app.get("/books/{language}")
async def read_book_by_category(language: str, category: str):
    books_to_return = []
    for book in books:
        if book.get('category').casefold() == category.casefold() and book.get('language').casefold() == language.casefold():
            books_to_return.append(book.get('title'))
    return books_to_return