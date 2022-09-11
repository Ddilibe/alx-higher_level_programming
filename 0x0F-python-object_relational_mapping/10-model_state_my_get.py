#!/usr/bin/python3
"""
    Script that print the state object with the name passed as argument
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    jame = session.query(State).filter(State.name == str(sys.argv[4])).first()
    print(jame.id if jame else "Not Found")
    session.close()
