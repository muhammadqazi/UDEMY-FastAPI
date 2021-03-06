from typing import Optional
from fastapi import FastAPI, HTTPException, Request, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from starlette.responses import JSONResponse

app = FastAPI()


class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(
        title="Description of the book", max_length=100, min_length=1)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "11f4c2ea-1340-41f4-89f7-2852347bb0d1",
                "title": "Computer Science Pro",
                "author": "Codingwithroby",
                "description": "A very nice description of a book",
                "rating": 75
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(
        None, title="Description of the book",
        max_length=100,
        min_length=1
    )


BOOKS = []


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request,
                                            exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Hey, why do you want {exception.books_to_return} "
                            f"books? You need to read more!"}
    )


@app.get('/header')
async def read_header(random_header: Optional[str] = Header(None)):
    return {"Random-Header": random_header}


@app.post('/books/login')
async def books_login(book_id: UUID, username: str = Header(None), password: str = Header(None)):
    if username == "FastAPIUser" and password == "test1234!":
        for book in BOOKS:
            if book.id == book_id:
                return book
    raise HTTPException(status_code=401, detail={"Inavlid user"})


@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):

    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)
    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS


@app.get('/book/{book_id}')
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.get('/book/rating/{book_id}', response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.put('/book/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete('/book/{book_id}')
async def delete_book(book_id: UUID):

    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted'
    raise raise_exception_item_not_found()


@app.post('/', status_code=201)
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="71f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="31f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="41f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)


def raise_exception_item_not_found():
    return HTTPException(status_code=404, detail={"Item not found "}, headers={
        "X-HEADER_ERROR": "Nothing to be seen at uuid"})
