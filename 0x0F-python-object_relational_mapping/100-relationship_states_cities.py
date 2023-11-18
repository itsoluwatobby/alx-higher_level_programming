#!/usr/bin/python3
# Creates the State “California” with the City “San Francisco”
# from the database hbtn_0e_100_usa.
# Usage: ./100-relationship_states_cities.py

from sys import argv
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine
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
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(City(name='San Francisco', state=State(name='California')))
        session.commit()

        session.close()
