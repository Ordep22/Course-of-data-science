import sqlite3 as sq
import pandas as pd
try:
    
    dataBase = sq.connect("cap12_dsa.db")
    print("Connected")
except:
    print("Something went wrong!")