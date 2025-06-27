#!/usr/bin/python3
"""9-model_state_filter_a.py"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """main"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()

    for state in (session.query(State)
                         .filter(State.name.like('%a%'))
                         .order_by(State.id)):
        print("{}: {}".format(state.id, state.name))
    session.close()
