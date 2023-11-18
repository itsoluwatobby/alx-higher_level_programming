#!/usr/bin/python3
# SQL INJECTION
# a script that takes in an argument and displays all values in the
#   states table of hbtn_0e_0_usa where name matches the argument.
import sys
import MySQLdb

if __name__ == "__main__":

    args = sys.argv[1:]
    try:
        if not len(args) or len(args) > 4:
            raise Exception('Bad entries')
    except Exception as e:
        print(e)
    else:
        uname, pwd, dbname, sname = args[0], args[1], args[2], args[3]
        name = sname.split("'")[0]

        conn = MySQLdb.connect(host='localhost', port=3306, user=uname,
                password=pwd, db=dbname, charset='utf8')
        cur = conn.cursor()
        cur.execute(
                "SELECT * FROM states as s WHERE name = '{}' ORDER BY s.id ASC"
                .format(name))
        queries = cur.fetchall()
        for query in queries:
            print(query)

        cur.close()
        conn.close()
