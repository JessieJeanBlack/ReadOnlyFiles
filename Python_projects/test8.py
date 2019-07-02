import sqlite3

conn = sqlite3.connect('test.db')
#conn will hold our database.

with conn:
    cur = conn.cursor()
    #cursor is going to actually operate. Invoke cursor with cur!
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                    ('Jessie', 'Black', 'jessie.james.black@gmail.com'))
        cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                    ('Sam', 'Pearce', 'slblack@gmail.com'))
        cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                    ('Richard', 'Smith', 'smithencryption@gmail.com'))
        cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                    ('Christina', 'Nosari', 'christinano@gmail.com'))
        conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Christina'")
    varPerson = cur.fetchall()#if using one, use collect one instead of collect all!
    for item in varPerson:
        msg = "First Name: () \nLast Name: () \nEmail: ()".format(item[0], item[1], item[2])
    print(msg)
        
        

