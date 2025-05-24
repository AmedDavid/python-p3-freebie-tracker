#!/usr/bin/env python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    # Use absolute path to ensure correct database location
    db_path = os.path.join(os.path.dirname(__file__), 'freebies.db')
    engine = create_engine(f'sqlite:///{db_path}')
    Session = sessionmaker(bind=engine)
    session = Session()
    import ipdb; ipdb.set_trace()