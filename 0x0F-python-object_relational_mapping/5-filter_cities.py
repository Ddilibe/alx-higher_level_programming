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
        "password": vari[2],
        "database": vari[3],
        "charset": "utf8",
    }
    conn = MySQLdb.connect(**instant)
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities, states\
            where cities.state_id = states.id and states.name = %s\
            ORDER BY cities.id ASC;", (vari[4],))
    query_rows = cur.fetchall()
    print(", ".join(jam[0] for jam in query_rows))
    cur.close()
    conn.close()
