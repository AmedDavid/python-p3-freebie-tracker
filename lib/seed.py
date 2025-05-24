#!/usr/bin/env python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Use absolute path to ensure correct database location
db_path = os.path.join(os.path.dirname(__file__), 'freebies.db')
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
company1 = Company(name="TechCorp", founding_year=1995)
company2 = Company(name="InnovateInc", founding_year=2000)
session.add_all([company1, company2])

# Create devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])

# Commit companies and devs to get IDs
session.commit()

# Create freebies
freebie1 = Freebie(item_name="T-Shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker", value=2, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Mug", value=15, dev=dev2, company=company1)
session.add_all([freebie1, freebie2, freebie3])

# Commit freebies
session.commit()

print("Database seeded successfully!")