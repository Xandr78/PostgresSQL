import psycopg2

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
def add_client(conn, name, surname, email, number=None):
    cur.execute("""
    insert into client (name, surname, email)
    values (%s, %s, %s);""", (name, surname, email))
    return cur.fetchone()

# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn, client_id, number):
    cur.execute("""
    insert into phones (client_id, number)
    values (%s, %s);""", (client_id, number))
    return cur.fetchone()

# Функция, позволяющая изменить данные о клиенте.
def change_client(conn, client_id, name=None, surname=None, email=None, number=None):
    cur.execute("""
    update client set name = %s, surname = %s, email = %s where id = %s;""", (name, surname, email, client_id))
    return cur.fetchone()

# Функция, позволяющая изменить телефон клиента.
def change_phone(conn, id, number):
    cur.execute("""
    update phones set number = %s where id = %s;""", (id, number))
    return cur.fetchone()

# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(conn, client_id, number):
    cur.execute("""
    delete from phones where client_id = %s;""", (client_id, number))
    return cur.fetchone()

# Функция, позволяющая удалить существующего клиента.
def delete_client(conn, id):
    cur.execute("""
    delete from clients where id = %s;""", (id))
    return cur.fetchone()

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(conn, name=None, surname=None, email=None, number=None):
    cur.execute("""
    select c.name, c.surname, c.email,  from clients c
    join phones p on p.client_id = c.id 
    where c.name = %s or c.surname = %s or c.email = %s or p.number = %s;""", (name, surname, email, number))
    return cur.fetchone()

with psycopg2.connect(database = "Clients", user = "postgres", password = "laima") as conn:
    with conn.cursor() as cur:
        # create_db(conn)
       print(add_client(conn, "Sam", "Vinchester", "hunting@rmail.com",))
        # print(add_phone(conn, 1, "12345678"))
        # print(change_client(conn, 1, "Sam", "Vinchester", "DANGERhunting@rmail.com"))
        # print(change_phone(conn, 1, "98765"))
        # print(delete_phone(conn, 1, "12345678"))
        # print(delete_client(conn,id))
        # print(find_client(conn, "Sam"))
    conn.commit()
conn.close()


