import psycopg2
from psycopg2.sql import SQL, Identifier
# Функция, создающая структуру БД (таблицы).
def create_db (conn):
        with conn.cursor() as cur:
            cur.execute("""
                DROP TABLE phones;
                DROP TABLE client;
            """)
            cur.execute("""
                create table if not exists client (id serial primary key,
                                                name varchar(40) unique,
                                                surname varchar(40) unique,
                                                email varchar(40) unique);
                                                """)
            cur.execute("""
                create table if not exists phones (id serial primary key,
                                                number varchar(20) unique,
                                                client_id integer not null references client (id));
                                                """)
            conn.commit()

# Функция, позволяющая добавить нового клиента.
def add_client(cur, name, surname, email):
    cur.execute("""
    insert into client (name, surname, email)
    values (%s, %s, %s) returning id, name, surname, email;""", (name, surname, email))


# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(cur, client_id, number):
    cur.execute("""
    insert into phones (client_id, number)
    values (%s, %s);""", (client_id, number))


# Функция, позволяющая изменить данные о клиенте.
#ВАРИАНТ1 - РАБОТАЕТ!
# def change_client(cur, id, name=None, surname=None, email=None):
#     cur.execute("""select * from client where id = %s""", (id, ))
#     current_user = cur.fetchone()
#     if name is None:
#         name = current_user[1]
#     if surname is None:
#         surname = current_user[2]
#     if email is None:
#         email = current_user[3]
#     cur.execute("""update client set name = %s, surname = %s, email = %s where id = %s""", (name, surname, email, id))

#ВАРИАНТ2 - РАБОТАЕТ!
# def change_client(cur, id, name=None, surname=None, e_mail=None):
#     arg_list = {'name': name, "surname": surname, 'e_mail': e_mail}
#     for key, arg in arg_list.items():
#         if arg:
#             cur.execute(SQL("UPDATE Client SET {}=%s WHERE id=%s").format(Identifier(key)), (arg, id))
#     cur.execute("""
#             SELECT * FROM Client
#             WHERE id=%s
#             """, id)
#     return cur.fetchall()

#ВАРИАНТ3 - РАБОТАЕТ!(обновляем данные сразу в обеих таблицах!)
def change_client(cur, id, name=None, surname=None, email=None, number=None):
    cur.execute("""select c.id, c.name, c.surname, c.email, p.number from client c
    join phones p on c.id = p.client_id
    where c.id = %s""", (id, ))
    current_user = cur.fetchone()
    if name is None:
        name = current_user[1]
    if surname is None:
        surname = current_user[2]
    if email is None:
        email = current_user[3]
    if number is None:
        number = current_user[4]
    cur.execute("""update client set name = %s, surname = %s, email = %s where id = %s""", (name, surname, email, id))
    cur.execute("""update phones set number = %s where client_id = %s""", (number, id))

# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(cur, number):
    cur.execute("""
    delete from phones where number = %s;""", (number, ))

# Функция, позволяющая удалить существующего клиента вместе с его телефоном.
def delete_client(cur, id):
    cur.execute("""
    delete from phones where client_id = %s;""", (id, ))
    cur.execute("""
    delete from client where id = %s;""", (id, ))

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
# def find_client(cur, name=None, surname=None, email=None, number=None):
#     cur.execute("""
#     select c.name, c.surname, c.email, p.number from client c
#     join phones p on p.client_id = c.id
#     where c.name = %s and c.surname = %s and c.email = %s and p.number = %s;""", (name, surname, email, number))
#     return cur.fetchone()

# def find_client(cur, name=None, surname=None, email=None, number=None):
#     print('Введите число  из перечня, как будет осуществляться поиск: "1"-по имени, "2"-по фамилии, "3"-"по email, "4"-по телефону')
#     while True:
#         surch1 = input("введите число: ")
#         if surch1 == 1:
#             cur.execute("""
#             select c.name, c.surname, c.email, p.number from client c
#             join phones p on p.client_id = c.id
#             where c.name = %s;""", (   name, ))
#             return cur.fetchone()
#             break
#         elif surch1 == 2:
#             cur.execute("""
#             select c.name, c.surname, c.email, p.number from client c
#             join phones p on p.client_id = c.id
#             where c.surname = %s;""", (surname, ))
#             return cur.fetchone()
#             break
#         elif surch1 == 3:
#             cur.execute("""
#             select c.name, c.surname, c.email, p.number from client c
#             join phones p on p.client_id = c.id
#             where c.email = %s;""", (email, ))
#             return cur.fetchone()
#             break
#         elif surch1 == 4:
#             cur.execute("""
#             select c.name, c.surname, c.email, p.number from client c
#             join phones p on p.client_id = c.id
#             where p.number = %s;""", (number, ))
#             return cur.fetchone()
#             break

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(cur, name=None, surname=None, email=None, number=None):
    if name is None:
        name = '%'
    else:
        name = '%' + name + '%'
    if surname is None:
        surname = '%'
    else:
        surname = '%' + surname + '%'
    if email is None:
        email = '%'
    else:
        email = '%' + email + '%'
    if number is None:
        cur.execute("""
            SELECT c.id, c.name, c.surname, c.email, p.number FROM client c
            JOIN phones p ON c.id = p.client_id
            WHERE c.name LIKE %s AND c.surname LIKE %s
            AND c.email LIKE %s
            """, (name, surname, email))
    else:
        cur.execute("""
            SELECT c.id, c.name, c.surname, c.email, p.number FROM client c
            JOIN phones p ON c.id = p.client_id
            WHERE c.name LIKE %s AND c.surname LIKE %s
            AND c.email LIKE %s AND p.number like %s
            """, (name, surname, email, number))
    return cur.fetchall()

#Проверка содержимого таблиц: client и phones
def check(cur):
    cur.execute("""
    select * from client;
    """)
    print(cur.fetchall())
    cur.execute("""
    select * from phones;
    """)
    print(cur.fetchall())

if __name__ == "__main__":
    with psycopg2.connect(database = "Clients", user = "postgres", password = "laima") as conn:
        with conn.cursor() as cur:
            # create_db(conn)
            # add_client(cur, "Alex", "Murrey", "Film@rmail.com")
            # add_phone(cur, 3, "5555555")
            # change_client(cur, '3', "aaa", "s", "dd", "222")
            # delete_phone(cur, "222")
            # delete_client(cur, 3)
            print(find_client(cur, 'Sam'))
            print(check(cur))
        # conn.commit()
    conn.close()


