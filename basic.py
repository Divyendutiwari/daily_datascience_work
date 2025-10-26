import sqlite3
connection=sqlite3.connect("example.db")
connection
cursor=connection.cursor()
cursor.execute('''
               create Table if not exists employee(
                   id Integer primary Key,
                   name text Not Null,
                   age Integer,
                   department text
               )
               ''')
cursor.execute('''
               Select * from employee
               
               ''')
cursor.execute('''
               Insert Into employee(name,age,department)
               values('bob',27,'Data Scientist')
               ''')
cursor.execute('''
               Insert Into employee(name,age,department)
               values('Krish',27,'Data Scientist')
               ''')
connection.commit()


cursor.execute('''
                   UPDATE employee
                   Set age=34
                   where name='bob'
                   ''')
connection.commit()
cursor.execute('Select * from employee')
rows=cursor.fetchall()
for row in rows:
    print(row)


