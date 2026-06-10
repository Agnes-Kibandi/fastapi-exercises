
from database import Base
from sqlalchemy import Integer,Column ,String
class Book(Base):
    __tablename__="books"
    id= Column(Integer,primary_key=True)
    title= Column(String)
    author=Column(String)
    year=Column(Integer)