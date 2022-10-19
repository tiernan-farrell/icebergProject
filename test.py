

import sqlite3


def main():
    print('hello')
    conn = sqlite3.connect('db/players.db')
    c = conn.cursor()
    res = c.execute("SELECT * FROM playerData;")
    print(res.fetchone())
    
    
if __name__ == "__main__":
    main()