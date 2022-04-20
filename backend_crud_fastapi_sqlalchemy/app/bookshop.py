from sqlalchemy.orm import Session
import models
import schemas


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, isbn: int):
    return db.query(models.Book).get(isbn)


def add_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, isbn: int, book: schemas.BookUpdate):
    db_book = db.query(models.Book).get(isbn)
    if db_book is None:
        raise Exception("Book not found")

    if book.author is None:
        book.author = db.query(models.Book).get(isbn).author

    if book.title is None:
        book.title = db.query(models.Book).get(isbn).title

    if book.price is None:
        book.price = db.query(models.Book).get(isbn).price

    db_book.author = book.author
    db_book.title = book.title
    db_book.price = book.price
    db.commit()
    return db_book


def delete_book(db: Session, isbn: int):
    db_book = db.query(models.Book).get(isbn)
    if db_book is None:
        raise Exception("Book not found")

    db.delete(db_book)
    db.commit()
    return {'message': 'Book deleted'}
