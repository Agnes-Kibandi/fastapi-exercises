
from database import Base
from sqlalchemy import Integer,Column ,String
class BookModel(Base):
    __tablename__="books"
    id= Column(Integer,primary_key=True)
    title= Column(String)
    author=Column(String)
    year=Column(Integer)



class ReaderModel(Base):
    __tablename__="readers"

    reader_id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    age=Column(Integer)
    hashed_password=Column(String)