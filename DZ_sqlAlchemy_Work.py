import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json
from pprint import pprint
# from DZ_sqlAlchemy_Class import create_tables, Publisher, Book
from DZ_sqlAlchemy_Class import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:laima@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind = engine)
session = Session()
#

with open("tests_data.json")  as f:
    data = json.load(f)
#     pprint(data)
#
for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    # session.add(model(id=record['pk'], **record.get('fields')))
session.commit()

session.query()

#РАБОТАЕТ!
def get_shops(s):
    if s.isdigit():
        for tb, ns, ps, ds in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == s).all():
            print(f"{tb:<40} {ns:<10} {ps:<8} {ds}")
    else:
        for tb, ns, ps, ds in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == s).all():
            print(f"{tb:<40} {ns:<10} {ps:<8} {ds}")

#НЕ РАБОТАЕТ!
# def get_shops(s):
#     if s.isdigit():
#         for tb, ns, ps, ds in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Book.books_publisher).join(Stock.stock_book).join(Sale.sale_stock).join(Shop.shop_stock).filter(Publisher.id == s).all():
#             print(f"{tb:<40} {ns:<10} {ps:<8} {ds}")
#     else:
#         for tb, ns, ps, ds in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == s).all():
#             print(f"{tb:<40} {ns:<10} {ps:<8} {ds}")


if __name__ == '__main__':
   s = input("Введите имя или айди публициста: ", )
   get_shops(s)

session.close()










#РАБОТАЕТ!
# s = input("Введите имя или айди публициста: ", )
# if s.isnumeric():
#     for p in session.query(Publisher).filter(Publisher.id == s).all():
#         print(p)
# else:
#     for p in session.query(Publisher).filter(Publisher.name == s).all():
#         print(p)

#РАБОТАЕТ!
# s = input("Введите имя или айди публициста: ", )
# if s.isdigit():
#     for p in session.query(Publisher).filter(Publisher.id == s).all():
#         print(p)
# else:
#     for p in session.query(Publisher).filter(Publisher.name == s).all():
#         print(p)

# for p in session.query(Publisher).filter(Publisher.name == "Pearson").all():
#     print(p)
# for p in session.query(Publisher).filter(Publisher.id == search()).all():
#     print(p)
# for b in session.query(Book).join(Book.books_connect).filter(Book.title.like('Nat%')).all():
#     print(b)

# #Вывод даных РАБОТАЕТ!
# s = input("Введите имя или айди публициста: ", )
# if s.isdigit():
#     for ses in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == s).all():
#         # print(str(ses[0]) + str(ses[1]) + str(ses[2]) + str(ses[3]))
#         print(ses)
# else:
#     for ses in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == s).all():
#         # print(str(ses[0]) + str(ses[1]) + str(ses[2]) + str(ses[3]))
#         print(ses)
