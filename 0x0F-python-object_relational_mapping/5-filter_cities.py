#!/usr/bin/python3
"""
    Script that takes a state as an argument and lista all the cities
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
    cur.execute("SELECT cities.name FROM cities, states\
            where cities.state_id = state.id and state.name = '{}'\
            ORDER BY cities.id ASC;".format(vari[4]))
    query_rows = cur.fetchall()
    for row in query_rows():
        print("({}, '{}')".format(row.id, row.name))
    cur.close()
    conn.close()
