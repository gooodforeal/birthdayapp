import sqlite3
import datetime


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        try:
            self.con = sqlite3.connect(db_name)
        except Exception as ex:
            print(ex)

    def sql_create_table(self):
        curs = self.con.cursor()
        ex = 'CREATE TABLE dates(id integer PRIMARY KEY, title text, date_of_birthday varchar(10))'
        curs.execute(ex)
        self.con.commit()

    def sql_insert_into_table(self, entities):
        curs = self.con.cursor()
        ex = 'INSERT INTO dates(title, date_of_birthday) VALUES(?, ?)'
        curs.execute(ex, entities)
        self.con.commit()

    def sql_get_by_date(self, arg_date):
        res = self.con.execute('SELECT * FROM dates WHERE date_of_birthday = ?', (arg_date,)).fetchone()
        return res



