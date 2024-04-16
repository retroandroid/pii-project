import sqlite3
import ast
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
    'City' TEXT,
    'Temperature' TEXT,
    'Humidity' TEXT,
    'Chance of Precipitation' TEXT,
    'Heat Index' TEXT,
    'Population' INTEGER
);"""

c.execute(stats)
c.executemany('INSERT INTO stats VALUES (?,?,?,?,?,?)',data)

connection.commit()
connection.close()

def load_data(city):
    connection = sqlite3.connect('temps.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM stats WHERE city = (?)", (city,))
    rows = cursor.fetchone()

    column_names = [column[0] for column in cursor.description]
    dicty = dict(zip(column_names, rows))

    for column, value in dicty.items():
        print(f"{column}: {value}")
        print('\n')


def filter(stat):
    connection = sqlite3.connect('temps.db')
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT city, "{stat}" FROM stats')
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]}: {row[1]}")
        print('\n')
