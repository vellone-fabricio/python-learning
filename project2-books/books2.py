from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", max_length=100, min_length=1)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            'example': {
                "id": "944c35c3-4ea2-4251-ac65-a669adc64305",
                "title": "blabla",
                "author": "Roberval",
                "description": "jasiodjasioj",
                "rating": 24
            }
        }
BOOKS = []

@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS)<1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        new_books = []
        for i in range(books_to_return):
            new_books.append(BOOKS[i])

        return new_books

    return BOOKS

@app.get('/book/{book_id}')
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x

@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted!'

def create_books_no_api():
    book_1 = Book(id="944c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd", rating=24)
    book_2 = Book(id="844c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd",rating=25)
    book_3 = Book(id="744c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd",rating=24)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
