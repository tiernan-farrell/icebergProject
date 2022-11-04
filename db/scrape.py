import requests
import sqlite3
from bs4 import BeautifulSoup


# This file scraps data on rb stats from 2021 from the url below with different RB's. 
# This data is added to the players.db sqlite3 db 

URL = 'https://www.pro-football-reference.com/players/'
YEAR = '/gamelog/2021/'

def get_stats(player):
    endPoint = URL + player + YEAR
    response = requests.get(endPoint)
    return response.content


def get_stat_value_from_game(game, pfr_stat_id):
    """
    Function that extracts a specific stat from a set of game stats
    :param game: Table Row extracted by BeautifulSoup
                 containing all player's stats for single game
    :param pfr_stat_id: PFR string element ID for the stat we want to extract
    :return: Extracted stat for provided game
    """
    data_stat_rec = game.find("td", {"data-stat": pfr_stat_id})
    if data_stat_rec is None: 
        return 0
    stat_val = data_stat_rec.renderContents().strip()
    return stat_val.decode("utf-8")


if __name__ == "__main__": 
    conn = sqlite3.connect('db/players.db')
    c = conn.cursor()
    
   # 25 of the highest ranked fantasy fb rbs that played in 2021
    players = ['T/TaylJo02', 'E/EkelAu00', 'C/CookDa01', 'H/HenrDe00',
               'H/HarrNa00', 'S/SwifDA00', 'M/MixoJo00', 'K/KamaAl00',
               'B/BarkSa00', 'J/JoneAa00', 'F/FourLe00', 'W/WilllJa10',
               'C/ChubNi00', 'C/ConnJa00', 'E/ElliEz00', 'E/EtieTr00',
               'M/MontDa01', 'D/DillAJ00', 'A/AkerCa00', 'M/MitcEl00',
               'E/EdmoCh00', 'J/JacoJo01', 'G/GibsAn00', 'H/HuntKa00', 'S/SandMi01']
    
    stats = ['game_num', 'game_date', 'team', 'opp', 'game_result', 'rush_att', 'rush_yds', 'rush_yds_per_att', 'rush_td', 'targets', 'rec', 'rec_yds', 'rec_yds_per_rec', 'rec_td', 'catch_pct', 'rec_yds_per_tgt', 'all_td', 'scoring', 'fumbles', 'fumbles_lost', 'fumbles_forced', 'fumbles_rec', 'fumbles_rec_yds', 'fumbles_rec_td', 'offense', 'off_pct', 'defense', 'def_pct', 'special_teams', 'st_pct']
   
    for idx, player in enumerate(players): 
        player_data = requests.get(URL + player + '.htm')
        s = BeautifulSoup(player_data.content, "html.parser")
        title = str(s.title)
        split = title.split(' ')
        first_name = str(split[0]).split('>')[1]
        last_name = split[1]
        res = get_stats(player)
        soup = BeautifulSoup(res, "html.parser")
        game_stats = soup.find_all("tr", id=lambda x: x and x.startswith("stats."))
        for game in game_stats:
            cur_pfr_game = int(get_stat_value_from_game(game, "week_num"))
            id = int(str(idx) + str(cur_pfr_game))
            print(id)
            data = {"player_id": idx, "first_name": first_name, "last_name": last_name}
            for stat in stats: 
                val = get_stat_value_from_game(game, stat)
                if stat == 'game_date' or stat == 'team' or stat == 'opp' or stat == 'game_result':
                    val = str(str(val).split('>')[1]).split('<')[0]
                data[stat] = val
                
            sql = "INSERT INTO playerData(player_id, first_name, last_name, game_num, game_date, team, opp, game_result, rush_att, rush_yds, rush_yds_per_att, rush_td, targets, rec, rec_yds, rec_yds_per_rec, rec_td, catch_pct, rec_yds_per_tgt, all_td, scoring, fumbles, fumbles_lost, fumbles_forced, fumbles_rec, fumble_rec_yards, fumble_rec_tds, offense, off_pct, defense, def_ptc, special_teams, st_pct) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            try: 
                c.execute(sql, tuple(data.values()))
                conn.commit()
            except sqlite3.Error as error:
                print("Failed to insert multiple records into sqlite table", error)
            
            
            
    