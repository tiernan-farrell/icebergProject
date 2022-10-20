

import sqlite3


def main():
    print('hello')
    # conn = sqlite3.connect('db/players.db')
    # c = conn.cursor()
    # res = c.execute(" SELECT * FROM playerData;")
    # print(res.fetchone())
    t = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    c = [t[i] for i in range(0, 3)]
    print(c)
if __name__ == "__main__":
    main()