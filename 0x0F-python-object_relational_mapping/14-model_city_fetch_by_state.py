#!/usr/bin/python3
# Python file similar to model_state.py named model_city.py
# that contains the class definition of a City.

from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
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
        queries = session.query(City, State).filter(
                City.state_id == State.id).order_by(City.id).all()

        for city, state in queries:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()
