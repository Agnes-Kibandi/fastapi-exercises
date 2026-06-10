from fastapi import FastAPI, HTTPException
from typing import Optional

app=FastAPI()

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




