from typing import Optional

from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from starlette.responses import JSONResponse

class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return

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


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", max_length=100, min_length=1)


BOOKS = []

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={"Message": f"Negative number passed! Try with a positive number"}
    )


@app.post("/books/login")
async def book_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}


@app.get("/header")
async def read_header(random_header: Optional[str] = Header(None)):
    return {"Random-Header": random_header}


@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)

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
    raise raise_item_cannot_be_found_exception()

@app.get('/book/ratings/{book_id}', response_model=BookNoRating)
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()

@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_cannot_be_found_exception()

@app.post('/', status_code=status.HTTP_201_CREATED)
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
    raise raise_item_cannot_be_found_exception()

def create_books_no_api():
    book_1 = Book(id="944c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd", rating=24)
    book_2 = Book(id="844c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd",rating=25)
    book_3 = Book(id="744c35c3-4ea2-4251-ac65-a669adc64305", title="Title 1", author="Author 1", description="dpsdkpaskd",rating=24)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)

def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404, detail="book not found!", headers={
        "X-Header-Error": "Nothing to be seen at the UUID"
    })
