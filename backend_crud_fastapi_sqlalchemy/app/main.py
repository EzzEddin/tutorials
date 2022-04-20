from fastapi import FastAPI, Depends
import models
import bookshop
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/book/list")
def get_book_list(
    skip: int = 0,
    limit: int = 100,
    db: SessionLocal = Depends(get_db)
):
    return bookshop.get_books(db, skip=skip, limit=limit)


@app.get("/book/{isbn}")
def get_book(isbn: int, db: SessionLocal = Depends(get_db)):
    return bookshop.get_book(db, isbn=isbn)


@app.post("/book")
def add_book(book: schemas.BookCreate, db: SessionLocal = Depends(get_db)):
    return bookshop.add_book(db=db, book=book)


@app.put("/book/{isbn}")
def update_book(
    isbn: int,
    book: schemas.BookUpdate,
    db: SessionLocal = Depends(get_db)
):
    return bookshop.update_book(db=db, isbn=isbn, book=book)


@app.delete("/book/{isbn}")
def delete_book(isbn: int, db: SessionLocal = Depends(get_db)):
    return bookshop.delete_book(db=db, isbn=isbn)
