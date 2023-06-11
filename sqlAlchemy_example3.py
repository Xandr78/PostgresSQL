import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

# Составление модели классов SQLAlchemy по схеме

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=90), nullable=False, unique=True)

    def __str__(self):
        return f'Издатель {self.id}: {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=90), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Книга {self.id}: ({self.title}, {self.id_publisher})'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=80), nullable=False)

    def __str__(self):
        return f'Магазин {self.id}: {self.name}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'Акции {self.id}: ({self.count}, {self.id_book}, {self.id_shop})'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Продажа {self.id} : ({self.date_sale}, {self.count}, {self.id_stock})'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


#СЧИТЫВАНИЕ С ФАЙЛА JSON
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import json

from models import create_tables, Publisher, Book, Shop, Stock, Sale
from config import DB_URI


def create_db(data):
    DSN = DB_URI
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    session.close()


def fixtures_file():
    with open("fixtures/tests_data.json", encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data


if __name__ == "__main__":
    create_db(fixtures_file())


#ЗАПУСК ВЫБОРКИ
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import json
from config import DB_URI

from models import create_tables, Publisher, Book, Shop, Stock, Sale


def id_or_name(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return value


def session_open(flag=True):
    DSN = DB_URI
    engine = sq.create_engine(DSN)
    if flag:
        create_tables(engine)

    Session = sessionmaker(bind=engine)
    return Session()


def create_db(data):
    session = session_open()

    for item in data:
        if item['model'] == 'publisher':
            publisher = Publisher(
                name=item['fields']['name'],
                id=item['pk'])
            session.add(publisher)

        elif item['model'] == 'book':
            book = Book(
                id=item['pk'],
                title=item['fields']['title'],
                id_publisher=item['fields']['id_publisher'])
            session.add(book)

        elif item['model'] == 'shop':
            shop = Shop(
                id=item['pk'],
                name=item['fields']['name'])
            session.add(shop)

        elif item['model'] == 'stock':
            stock = Stock(
                id=item['pk'],
                id_book=item['fields']['id_book'],
                id_shop=item['fields']['id_shop'],
                count=item['fields']['count'])
            session.add(stock)

        elif item['model'] == 'sale':
            sale = Sale(
                id=item['pk'],
                price=item['fields']['price'],
                date_sale=item['fields']['date_sale'],
                id_stock=item['fields']['id_stock'],
                count=item['fields']['count'])
            session.add(sale)
        session.commit()
    session.close()


def book_sale(ask_publisher):
    session = session_open(False)
    ask_publisher = id_or_name(ask_publisher)
    if type(ask_publisher) == str:
        id_publisher = session.query(Publisher.id).filter(Publisher.name == ask_publisher).scalar()
    else:
        id_publisher = ask_publisher
    if id_publisher:
        for item in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Sale.stock) \
                .join(Stock.shop).join(Stock.book).filter(Book.id_publisher == id_publisher).all():
            print_list = list(item)
            print(f"{print_list[0]:<20}|\t"
                  f"{print_list[1]:<15}|\t"
                  f"{int(print_list[2]):<9}|\t"
                  f"{print_list[3].strftime('%d-%m-%Y')}")
    else:
        print('Publisher not found')

    session.close()


def fixtures_file():
    with open("fixtures/tests_data.json", encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data


if __name__ == "__main__":
    create_db(fixtures_file())
    book_sale(input('Введите имя либо идентификатор издателя: '))
