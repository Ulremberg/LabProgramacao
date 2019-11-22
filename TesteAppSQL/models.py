import sqlite3 as sql


def insert_user(username):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username) VALUES (?,?)"(username))
    con.commit()
    con.close()


def retrieve_users():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username FROM users")
    users = cur.fetchall()
    con.close()
    return users
