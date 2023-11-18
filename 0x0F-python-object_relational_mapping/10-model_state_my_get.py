#!/usr/bin/python3
"""
a script that prints the State object with the "name" passed as argument
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = argv[1:]
    try:
        if not len(args) or len(args) > 4:
            raise Exception('Bad Entries')
    except Exception as e:
        print(e)
    else:
        uname, pwd, dbname, sname = args[0], args[1], args[2], args[3]
        name = sname.split("'")[0]

        sql = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                uname, pwd, dbname)
        engine = create_engine(sql, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).filter(
                State.name == name).order_by(State.id).all()
        if not len(states):
            print('Not found')
        else:
            for state in states:
                print("{}".format(state.id))
        session.close()
