from ensurepip import bootstrap
from turtle import pos
from typing import Optional
from unittest import skip
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get('/')
async def first_api():
    return BOOKS

# This is path parameter which starts with /East


@app.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "Sub": "UP"}
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "Sub": "DOWN"}
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "Sub": "LEFT"}
    return {"Direction": direction_name, "Sub": "RIGHT"}


# This is query parameter which starts with /?book_3
@app.get('/skipbook')
# default value is book_3
async def skip_books(skip_book: Optional[str] = "book_3"):
    if skip_book:
        new_book = BOOKS.copy()
        del new_book[skip_book]
        return new_book
    return BOOKS


@app.get('/{book_name}')
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post('/')
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id+1}'] = {'title': book_title,
                                          'author': book_author}
    return BOOKS[f'book_{current_book_id+1}']


@app.put('/{book_name}')
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {"title" : book_title , "author" : book_author}
    BOOKS[book_name] = book_information
    return book_information

@app.delete('/{book_name}')
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'
