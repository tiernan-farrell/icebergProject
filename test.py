

import sqlite3


def main():
    print('hello')
    # conn = sqlite3.connect('db/players.db')
    # c = conn.cursor()
    # res = c.execute(" SELECT * FROM playerData;")
    # print(res.fetchone())
    t = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

    print(t.replace(0, 4))
if __name__ == "__main__":
    main()