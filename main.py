###**Exercise one.** Create a brand new FastAPI project from scratch. Just `main.py`. No database. No auth. Just the basics. Create three endpoints. A root endpoint that returns your name. A `/hobbies` endpoint that returns a list of your hobbies. A `/bio` endpoint that returns a few facts about yourself.

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def name():
    my_name="Agnes"
    return my_name

@app.get("/hobbies")
def hobbies():
    my_hobbies=['coding','swimming','fashion','dancing']
    return my_hobbies

@app.get("/bio")
def fun_facts():
    my_fun_facts={'gender':'female','age':37}
    return my_fun_facts
