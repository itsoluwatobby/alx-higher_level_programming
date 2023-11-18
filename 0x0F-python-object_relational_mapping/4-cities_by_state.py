#!/usr/bin/python3
# a script that lists all cities from the database hbtn_0e_4_usa
import sys
import MySQLdb

if __name__ == "__main__":

    args = sys.argv[1:]
    try:
        if not len(args) or len(args) > 3:
            raise Exception('Bad Entries')
    except Exception as e:
        print(e)
    else:
        uname, pwd, dbname = args[0], args[1], args[2]

        conn = MySQLdb.connect(
                host='localhost',
                port=3306, user=uname,
                password=pwd, db=dbname,
                charset='utf8')
        cur = conn.cursor()
        sql="""SELECT c.id, c.name, s.name FROM cities AS c, states AS s 
        WHERE c.state_id = s.id ORDER BY c.id ASC"""
        cur.execute(sql)
        queries = cur.fetchall()
        for query in queries:
            print(query)

        cur.close()
        conn.close()
