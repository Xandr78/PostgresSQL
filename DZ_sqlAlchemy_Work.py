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

# with open("tests_data.json")  as f:
#     data = json.load(f)
#     pprint(data)
#
#
session.close()
