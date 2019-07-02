import sqlite3
from sqlite3 import Error
 
 
def create_connection(my_Python):
    """ create a database connection to a SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(my_Python)
    except Error as e:
        print(e)
      

def create_table(conn, tbl_data):
    """ create a table from the tbl_data statement
    :param conn: Connection object
    :param tbl_data: a CREATE TABLE statement
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(tbl_data)
    except Error as e:
        print(e)

def main():
    database = "C:\Python_projects\my_Python.db"
 
    tbl_data = """ CREATE TABLE IF NOT EXISTS tbl_Py (
                                        id integer PRIMARY KEY,
                                        NAME text NOT NULL
                                    ); """
import sqlite3
conn = sqlite3.connect('my_Python.db')
conn.commit()
conn.close()


if __name__ == '__main__':
    create_connection("C:\Python_projects\my_Python.db")
