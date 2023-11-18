#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Selects records from the command line"""
    args = sys.argv[1:]
    try:
        if not len(args) or len(args) > 4:
            raise Exception('Bad Entries')
    except Exception as e:
        print(e)
    else:
        uname, pwd, dbname, sname = args[0], args[1], args[2], args[3]
        name = sname.split(",")[0]

        conn = MySQLdb.connect(
                host='localhost', port=3306,
                user=uname, password=pwd,
                db=dbname, charset='utf8')
        cur = conn.cursor()
        sql = """ SELECT cities.name FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s ORDER BY cities.id ASC """
        cur.execute(sql, (name,))
        queries = cur.fetchall()
        print(", ".join([city[0] for city in queries]))
        cur.close()
        conn.close()
