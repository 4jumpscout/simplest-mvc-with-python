import pandas as pd
import view
import controller
db=pd.read_json("persons.json")
def spesifik_kisi():
    y=int(input())
    if y==0:
        return tam()
    else:
        a=str(db[y:y+1])
        return view.spes(a)
def tam():
    x=str(db)
    return view.tamitam(x)





