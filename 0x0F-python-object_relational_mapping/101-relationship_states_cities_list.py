#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
Your script should take 3 arguments:
<mysql username>, <mysql password>, <database name>
"""
from sys import argv
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Selects records from the command line"""
    args = argv[1:]
    try:
        if not len(args) or len(args) > 3:
            raise Exception('Bad Entries')
    except Exception as e:
        print(e)
    else:
        uname, pwd, dbname = args[0], args[1], args[2]
        sql = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                uname, pwd, dbname)
        engine = create_engine(sql, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("     {}: {}".format(city.id, city.name))
        session.close()
