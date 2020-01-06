import sqlite3

conn = sqlite3.connect("collect.db")


def creat_table():
    cur = conn.cursor()
    cur.execute(
        "create table m_string (id integer PRIMARY KEY autoincrement, userid varchar (20),img varchar(20),ext varchar (20),content varchar (20),sid varchar (20))")
    cur.close()


def get_strings():
    cur = conn.cursor()
    cur.execute("select * from m_string")
    return cur.fetchall()


def add_string(userid, img, ext, content, sid):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO m_string (userid,img,ext,content,sid) VALUES ('%s','%s','%s','%s','%s')" % (
            userid, img, ext, content, sid))
    conn.commit()
    cur.close()
