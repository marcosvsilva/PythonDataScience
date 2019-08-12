import os
import random
import sqlite3
import datetime
import matplotlib.pyplot as plt

bd_name = "supermarket.db"
os.remove(bd_name) if os.path.exists(bd_name) else None
con = sqlite3.connect(bd_name)
cur = con.cursor()


def create_table_moviment():
    create_table = 'create table moviment (' \
                   'id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
                   'date    TEXT NOT NULL,' \
                   'product INTEGER NOT NULL,' \
                   'value   NUMERIC)'

    cur.execute(create_table)
    con.commit()

    popule_moviment()


def popule_moviment():
    sql_insert = 'insert into moviment (date, product, value) values(?, ?, ?)'

    for i in range(10):
        value = random.randrange(0, 400)
        date = datetime.date.today()
        insert_line = [date.strftime("%d/%m/%Y"), i, value]
        cur.execute(sql_insert, insert_line)

    con.commit()


def select_database(select):
    try:
        cur.execute(select)
        return cur.fetchall()
    finally:
        cur.close()
        con.close()


create_table_moviment()

select = 'select * from moviment'
data = select_database(select)

products = []
values = []
for register in data:
    products.append(register[2])
    values.append(register[3])

plt.bar(products, values)
plt.show()
