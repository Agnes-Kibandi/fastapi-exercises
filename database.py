
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url="sqlite:///./my_db.db"

engine=create_engine(database_url)
SessionLocal=sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base=declarative_base()