import sqlite3

conn = sqlite3.connect('db/players.db')

c = conn.cursor()

c.execute("""CREATE TABLE players (
            firstName text, 
            lastName text 
            )""")



