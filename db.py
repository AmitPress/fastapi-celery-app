from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://amit:12345@localhost:5432/aslpm')

conn = engine.connect()

Base = declarative_base()

local_session = sessionmaker(engine)
session = local_session()