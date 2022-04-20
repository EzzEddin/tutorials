from optparse import Option
from typing import Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    author: str
    title: str
    price: Optional[float] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    author: Optional[str] = None
    title: Optional[str] = None


class Book(BookBase):
    isbn: int

    class Config:
        orm_mode = True
