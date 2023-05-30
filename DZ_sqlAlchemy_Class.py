import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)
    publisher_book = relationship('Book', back_populates="books_publisher")
    def __str__(self):
        return f'publisher {self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    # publisher = relationship('Publisher', backref = 'book')
    books_publisher = relationship('Publisher', back_populates= "publisher_book")
    book_stock = relationship('Stock', back_populates= "stock_book")
    def __str__(self):
        return f'book {self.id}: {self.title}, {self.id_publisher}'
#
class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    shop_stock = relationship('Stock', back_populates= "stock_shop")
    def __str__(self):
        return f'shop {self.id}: {self.name}'

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    stock_shop = relationship('Shop', back_populates= "shop_stock")
    stock_book = relationship('Book', back_populates= "book_stock")
    stock_sale = relationship('Sale', back_populates= "sale_stock")
    # stock_book = relationship('Book', backref = 'stock')
    # stock_shop = relationship('Shop', backref = 'stock2')
    def __str__(self):
        return f'stock {self.id}: {self.count}, {self.id_book}, {self.id_shop}'

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    sale_stock = relationship('Stock', back_populates= "stock_sale")
    # sale_stock = relationship('Stock', backref = 'sale')
    def __str__(self):
        return f'sale {self.id}: {self.price}, {self.date_sale}, {self.count}, {self.id_stock}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)







