

from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel
from models import BookModel,ReaderModel
from database import engine,SessionLocal,Base
from auth import password_checker,password_scrambler,token_generator,token_verifier
from fastapi.security import OAuth2PasswordRequestForm

Base.metadata.create_all(bind=engine)

app=FastAPI()

class Book(BaseModel):
    title:str
    author:str
    year:int

class BookOut(BaseModel):
    title:str
    author:str

class ReaderIn(BaseModel):
    name:str
    email:str
    age:int 
    password:str

class ReaderOut(BaseModel):
    name:str
    email:str
    age:int 


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/reader",response_model=ReaderOut)
def reader_signup(reader:ReaderIn,db=Depends(get_db)):
    hashed=password_scrambler(reader.password)

    new_reader=ReaderModel( name=reader.name,email=reader.email,age=reader.age,hashed_password=hashed)

    db.add(new_reader)
    db.commit()
    db.refresh(new_reader)

    return new_reader

@app.post("/login")
def reader_login(form_data:OAuth2PasswordRequestForm= Depends(),db=Depends(get_db)):
    username=form_data.username
    password=form_data.password

    user=db.query(ReaderModel).filter(ReaderModel.name==username).first()
    if user is None:
        raise HTTPException(status_code=401,detail="invalid credentials")
    is_valid=password_checker(password,user.hashed_password)
    if not is_valid:
        raise HTTPException(status_code=401,detail="invalid credentials")
    return {"access_token":token_generator({"sub":username}),"token_type":"bearer"}

    

@app.post("/books",response_model=BookOut)
def save_book(book:Book, db=Depends(get_db)):
    db_book=BookModel(title=book.title,author=book.author,year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/{book_id}",response_model=BookOut)
def specific_book(book_id:int,db=Depends(get_db)):
        
    the_book=db.query(BookModel).filter(BookModel.id==book_id).first()

    if not the_book:
        raise  HTTPException(status_code=404,detail="not found")
    return the_book



@app.get("/books",response_model=list[BookOut])
def get_books(db=Depends(get_db)):
    the_books=db.query(BookModel).all()
    return the_books
    
    

@app.get("/")
def name():
    my_name="Agnes"
    return my_name

@app.get("/hobbies/{hobby_id}")
def hobbies(hobby_id:int):
    try:
        my_hobbies=['coding','swimming','fashion','dancing']
        return my_hobbies[hobby_id]
    except IndexError:
        raise HTTPException(status_code=404,detail="no hobby exists")

@app.get("/bio")
def fun_facts():
    my_fun_facts={'gender':'female','age':37}
    return my_fun_facts

@app.get("/search")
def search_results(keyword: str="Nothing"):
    return f" you searched for {keyword}."




