#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
hbtn_0e_6_usa
"""
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

        sql = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                uname, pwd, dbname)
        engine = create_engine(sql, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        target = session.query(State).filter(State.id == 2).first() 
        target.name = 'New Mexico'
        session.add(target)
        session.commit()
        session.close()
