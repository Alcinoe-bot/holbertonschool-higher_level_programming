#!/usr/bin/python3
"""
5-filter_cities.py
"""
import MySQLdb
import sys


if __name__ == "__main__":
    "main"
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (sys.argv[4],))

    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
