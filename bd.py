import sqlite3
import os


class DataBase:
    _db = None

    def __new__(cls, *args, **kwargs):
        if cls._db is None:
            cls._db = super().__new__(cls)
        return cls._db

    def __init__(self, db_path: str = 'database/my_db.db'):
        self._db_path = db_path

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = sqlite3.connect(self._db_path)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table(self, table_name: str):
        sql_table = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT,
                    user_phone TEXT,
                    comment TEXT
                    )'''
        self.execute(sql_table)

    def add_user(self, name, phone, comment):
        sql_insert = f'''INSERT INTO my_first_table (user_name, user_phone, comment) VALUES (?, ?, ?)'''
        self.execute(sql_insert, (name, phone, comment), commit=True)

    #
    # def get_row(connect, cursor, user_name: str, _all: bool = False):
    #     sql_select = '''SELECT * FROM my_first_table WHERE user_name=?'''
    #     cursor.execute(sql_select, (user_name,))
    #     return cursor.fetchall() if _all else cursor.fetchone()
    #
    # @open_db
    # def update_row(connect, cursor, new_phone: str, user_id: int):
    #     sql_update = '''UPDATE my_first_table SET user_phone=? WHERE user_id=?'''
    #     cursor.execute(sql_update, (new_phone, user_id))
    #     connect.commit()
    #
    # @open_db
    # def delete_row(connect, cursor, user_id: int):
    #     sql_delete = 'DELETE FROM my_first_table WHERE user_id=?'
    #     cursor.execute(sql_delete, (user_id,))
    #     connect.commit()
