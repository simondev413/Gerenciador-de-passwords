import sqlite3

db = sqlite3.connect('mydb.db')
cursor = db.cursor()
cursor.execute('create table if not exists password(id int not null primary key,pwd varchar(50) not null unique,account varchar(50))')

class DB:

    def generateID():
        cursor.execute('select id from password')
        id = cursor.fetchall()
        db.commit()
        if len(id) == 0:
            return 1
        return   id[-1][0] + 1

    def insert(account,pwd):
        cursor.execute(f"insert into password values('{DB.generateID()}','{pwd}','{account}')")
        db.commit()

    def get():
        cursor.execute('select * from password')
        dados = cursor.fetchall()
        return dados if dados else  'No data retrieved'   