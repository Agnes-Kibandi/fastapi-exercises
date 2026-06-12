

from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel
from models import BookModel
from database import engine,SessionLocal,Base

Base.metadata.create_all(bind=engine)

app=FastAPI()

class Book(BaseModel):
    title:str
    author:str
    year:int

class BookOut(BaseModel):
    title:str
    author:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

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




