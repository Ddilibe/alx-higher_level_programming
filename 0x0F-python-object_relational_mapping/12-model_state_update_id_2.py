#!/usr/bin/python3
"""
    Script that changes the name of the state oject from the database
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    jame = session.query(State).filter(State.id == 2).first()
    jame.name = "New Mexico"
    session.commit()
    session.close()
