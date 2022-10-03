#!/usr/bin/python3
"""
    Module for Listing all the cities from the database
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
            cities JOIN states ON cities.state_id = states.id\
            ORDER BY state_id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
