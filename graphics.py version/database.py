import sqlite3

class Database():
    def __init__(self, dbname: str):
        if dbname == '':
            self.dbname = "RobotControl"
        else:
            self.dbname = dbname

        self.db_connection = sqlite3.connect(self.dbname)
        self.db_cursor = self.db_connection.cursor()

    def commit(self, sql_cmd):
        self.db_cursor.execute(sql_cmd)
        self.db_connection.commit()
