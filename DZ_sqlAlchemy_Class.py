import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)
    publisher_connect = relationship('Book', back_populates="books_connect")
    def __str__(self):
        return f'publisher {self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    id_published = sq.Column(sq.Integer, sq.ForeignKey('published.id'), nullable=False)
    # publisher = relationship(Publisher, backref = 'book')
    books_connect = relationship('Publisher', back_populates= "published_connect")
    def __str__(self):
        return f'book {self.id}: {self.title}, {self.id_published}'
#
class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    def __str__(self):
        return f'shop {self.id}: {self.name}'

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    book = relationship(Book, backref = 'stock')
    shop = relationship(Shop, backref = 'stock')
    def __str__(self):
        return f'stock {self.id}: {self.count}, {self.id_book}, {self.id_shop}'

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Integer)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    stock = relationship(Stock, backref = 'sale')
    def __str__(self):
        return f'sale {self.id}: {self.price}, {self.date_sale}, {self.count}, {self.id_stock}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# DSN = 'postgresql://postgres:laima@localhost:5432/books'
# engine = sqlalchemy.create_engine(DSN)
# create_tables(engine)
# Session = sessionmaker(bind = engine)
# session = Session()



session.close()
