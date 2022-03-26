from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Ex 1', 'auth': 'auth one'},
    'book_2': {'title': 'Ex 2', 'auth': 'auth two'},
    'book_3': {'title': 'Ex 3', 'auth': 'auth three'},
    'book_4': {'title': 'Ex 4', 'auth': 'auth four'},
    'book_5': {'title': 'Ex 5', 'auth': 'auth five'},
}

@app.get("/")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def get_a_book(book_title):
    return BOOKS[book_title]


class Directions(str, Enum):
    North = 'North'
    South = 'South'
    East = 'East'
    West = 'West'

@app.get('/directions/{directions}')
async def get_dir(directions: Directions):
    if directions.name == directions.North:
        return {f'Here we go to the {directions.name}!\n, up then!'}
    elif directions.name == directions.South:
        return {f'Here we go to the {directions.name}!\n, down then!'}
    elif directions.name == directions.East:
        return {f'Here we go to the {directions.name}!\n, right then!'}
    elif directions.name == directions.West:
        return {f'Here we go to the {directions.name}!\n, left then!'}
