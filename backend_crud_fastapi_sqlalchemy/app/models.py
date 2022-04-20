from sqlalchemy import Column, Integer, String, Float
from database import Base


class Book(Base):
    __tablename__ = 'books'
    isbn = Column(Integer, primary_key=True)
    author = Column(String(100))
    title = Column(String(100))
    price = Column(Float)

    def to_json(self):
        return {
            'isbn': self.isbn,
            'author': self.author,
            'title': self.title,
            'price': self.price
        }
