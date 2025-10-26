import sqlite3
connection=sqlite3.connect('sale_data.db')
cursor=connection.cursor()
cursor.execute('''
               create table if not exists sales(
                  
                  date TEXT NOT NULL,
                  product TEXT NOT NULL,
                  sales INTEGER NOT NULL,
                  region TEXT
                   
               )
               ''')
sale_data=[
    ('2023-01-01','product1',100,'North'),
    ('2023-01-01','product2',100,'North')
    
]
cursor.executemany('''
               Insert into sales(date,product,sales,region)
               values(?,?,?,?)
               ''',sale_data)
connection.commit()
cursor.execute('select * from sales')
rows=cursor.fetchall()
for row in rows:
    print(row)