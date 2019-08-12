import os
import sqlite3

bd_name = "school.db"
os.remove(bd_name) if os.path.exists(bd_name) else None

con = sqlite3.connect(bd_name)
cur = con.cursor()

print(type(cur))

sql_create = 'create table course ' \
             '(id integer primary key, ' \
             'title varchar(100), ' \
             'category varchar(140))'

cur.execute(sql_create)
con.commit()

sql_insert = 'insert into course values(?, ?, ?)'

insert_register = [(1001, 'course 1', 'course1'),
                   (1002, 'course 2', 'course2'),
                   (1003, 'course 3', 'course3')]

for register in insert_register:
    cur.execute(sql_insert, register)

con.commit()

sql_select = 'select * from course'

cur.execute(sql_select)
data = cur.fetchall()

for line in data:
    print("Register course - id: %d, name: %s, department: %s." % line)

cur.close()
con.close()
