import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        try:
            self.con = sqlite3.connect(db_name)
        except Exception as ex:
            print(ex)

    def sql_create_table(self):
        curs = self.con.cursor()
        ex = 'CREATE TABLE dates(id integer PRIMARY KEY, title text, date_of_birthday date)'
        curs.execute(ex)
        self.con.commit()

    def sql_insert_into_table(self, entities):
        curs = self.con.cursor()
        ex = 'INSERT INTO dates(id, title, date_of_birthday) VALUES(?, ?, ?)'
        curs.execute(ex, entities)
        self.con.commit()

