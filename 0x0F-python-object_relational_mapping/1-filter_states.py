#!/usr/bin/python3
# a script that lists all states with a name starting with N (upper N) from
#   the database hbtn_0e_0_usa:
import sys
import MySQLdb

if __name__ == "__main__":

    args = sys.argv[1:]
    uname, pwd, dbname = args[0], args[1], args[2]

    conn = MySQLdb.connect(
            host='localhost',
            port=3306, user=uname,
            password=pwd, db=dbname,
            charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    queries = cur.fetchall()
    for query in queries:
        print(query)

    cur.close()
    conn.close()
