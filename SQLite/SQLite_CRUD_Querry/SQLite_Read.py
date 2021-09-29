import sqlite3
import sys
import traceback
from SQLite.SQLite_CRUD_Querry.SQLite_Create_Tables import db_name


def sqlite_read_col_in_table(table, col):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        cursor = sqlite_connection.cursor()
        # print('DB connect in SQLite')
        cursor.execute(f"SELECT {col} FROM {table} WHERE id IN(SELECT max(id) FROM {table} );")
        result = cursor.fetchall()
        # print(f"Запись успешно прочитана в таблице {table} ", cursor.rowcount)
        cursor.close()
        for ar in result:
            for lst in ar:
                # print(lst)
                return lst
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error} (read)")
        # print("Не удалось прочитать данные в таблице sqlite")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Close connection")


def sqlite_count(table):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        cursor = sqlite_connection.cursor()
        # print('DB connect in SQLite')
        # cursor.execute(f"SELECT * FROM {table};")
        result = len(cursor.execute(f"SELECT * FROM {table};").fetchall())
        # print(f"В таблице {table} сейчас {result} записей", cursor.rowcount)
        cursor.close()
        return int(result)
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error} (read)")
        # print("Не удалось посчитать записи в таблице sqlite")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Close connection")
