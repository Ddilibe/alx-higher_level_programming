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
        "passwd": vari[2],
        "db": vari[3],
        "charset": "utf8",
    }
    conn = MySQLdb._mysql.connect(**instant)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{}'\
            ORDER BY states.id ASC".format(
            vari[4]
        )
    )
    query_rows = cur.fetchall()
    for row in query_rows():
        print("({}, '{}')".format(row.id, row.name))
    cur.close()
    conn.close()
