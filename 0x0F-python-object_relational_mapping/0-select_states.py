#!/usr/bin/python3
"""
    Module for ORM to interact with MySQL database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    vari = sys.argv
    instant = {
        "host": "localhost",
        "port": 3306,
        "user": vari[1],
        "password": vari[2],
        "database": vari[3],
        "charset": "utf8",
    }
    conn = MySQLdb.connect(**instant)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
