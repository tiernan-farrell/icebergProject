import sqlite3

conn = sqlite3.connect('db/players.db')

c = conn.cursor()

c.execute("""CREATE TABLE playerData (
            player_week_id INTEGER PRIMARY KEY,
            player_id INTEGER, 
            first_name TEXT NOT NULL, 
            last_name TEXT NOT NULL,
            game_num INTEGER, 
            game_date TEXT,
            team TEXT,
            opp TEXT,
            game_result TEXT,
            rush_att INTEGER, 
            rush_yds INTEGER, 
            rush_yds_per_att REAL, 
            rush_td INTEGER, 
            targets INTEGER,
            rec INTEGER, 
            rec_yds INTEGER,
            rec_yds_per_rec REAL,
            rec_td INTEGER,
            catch_pct TEXT,
            rec_yds_per_tgt REAL,
            all_td INTEGER,
            scoring INTEGER,
            fumbles INTEGER,
            fumbles_lost INTEGER,
            fumbles_forced INTEGER,
            fumbles_rec INTEGER,
            fumble_rec_yards INTEGER,
            fumble_rec_tds INTEGER,
            offense INTEGER,
            off_pct TEXT,
            defense INTEGER,
            def_ptc TEXT,
            special_teams INTEGER,
            st_pct TEXT
            )""")

