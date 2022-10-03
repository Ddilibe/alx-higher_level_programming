#!/usr/bin/python3
"""
    Script that prints all the city objects from the database
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    james = session.query(City).all()
    for i in james:
        h = session.query(State).filter(State.id == i.state_id).first()
        print("{}: ({}) {}".format(h.name, i.id, i.name))
    session.close()
