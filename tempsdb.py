import ast
import sqlite3
import webscrapper
webscrapper.itemstorer()

with open('base.txt', 'r') as f:
    contents = f.readlines()

listy = [i for i in map(ast.literal_eval, contents)]
data = [tuple(j) for j in listy]

connection = sqlite3.connect('temps.db')
c = connection.cursor()

c.execute('DROP TABLE IF EXISTS stats')

stats = """
    CREATE TABLE IF NOT EXISTS stats(
    city TEXT,
    temp_in_F TEXT,
    temp_in_C TEXT,
    humidity TEXT,
    chance_of_precipitation TEXT,
    heat_index_in_F INTEGER,
    heat_index_in_C INTEGER,
    population INTEGER
);"""

c.execute(stats)
c.executemany('INSERT INTO stats VALUES (?,?,?,?,?,?,?,?)',data)

connection.commit()
connection.close()