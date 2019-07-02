
def create_connection(my_Python):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(my_Python)
        return conn
    except Error as e:
        print(e)
 
    return None
