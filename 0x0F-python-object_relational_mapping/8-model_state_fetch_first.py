#!/usr/bin/python3
# a script that prints the first State object from the database hbtn_0e_6_usa
from sys import argv
from model_state import Base, State

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

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(uname, pwd, dbname), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).first()
        print("{}: {}".format(state.id, state.name))
        session.close()
