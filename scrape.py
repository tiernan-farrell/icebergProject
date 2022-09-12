import requests

from bs4 import BeautifulSoup


def get_stats():
    response = requests.get('https://www.pro-football-reference.com/players/M/MoorD.00/gamelog/')
    return response.content


def get_stat_for_season(html_game_stats, stat_to_scrape):
    """
    Function that extracts a given stat from PFR table rows 
    and returns the results in a list
    
    :param html_game_stats: BeautifulSoup PageElements containing our stats
    :param stat_to_scrape: PFR stat_id to extract
    :return: List of stats, 16-weeks big, for player's season
    """
    scraped_weekly_stats = []
    game_being_processed = 1
    for game in html_game_stats:
        cur_pfr_game = int(get_stat_value_from_game(game, "week_num"))

        if player_has_missed_games(game_being_processed, cur_pfr_game):
            scraped_weekly_stats = fill_in_missed_games(
                game_being_processed, cur_pfr_game, scraped_weekly_stats
            )

        game_receptions = get_stat_value_from_game(game, stat_to_scrape)
        scraped_weekly_stats.append(game_receptions)
        game_being_processed += 1

    check_if_missed_week_sixteen(scraped_weekly_stats)
    return scraped_weekly_stats


def get_stat_value_from_game(game, pfr_stat_id):
    """
    Function that extracts a specific stat from a set of game stats
    :param game: Table Row extracted by BeautifulSoup
                 containing all player's stats for single game
    :param pfr_stat_id: PFR string element ID for the stat we want to extract
    :return: Extracted stat for provided game
    """
    data_stat_rec = game.find("td", {"data-stat": pfr_stat_id})
    stat_val = data_stat_rec.renderContents().strip()
    return stat_val.decode("utf-8")
    
    
def player_has_missed_games(game_being_processed, cur_pfr_game):
    """
    Function that checks if the player has missing games
    :param game_being_processed: Game (by week) we are processing
    :param cur_pfr_game: Game (by week) we are on for the player
    :return: Bool
    """
    if game_being_processed == cur_pfr_game:
        return False

    return True

def fill_in_missed_games(game_being_processed, cur_pfr_game, stat_per_game):
    """
    Function that fills a list with 0s for missing games
    
    :param game_being_processed: Game (by week) we are processing
    :param cur_pfr_game: Game (by week) we are on for the player
    :param stat_per_game: List containing a stat's value for each game
    :return: Updated list with missing games filled in with "0"
    """
    games_missed = cur_pfr_game - game_being_processed
    for i in range(games_missed):
        stat_per_game.append("0")

    return stat_per_game


def check_if_missed_week_sixteen(stat_per_game):
    """
    Function that checks a list of stats per game is the
    expected 16 weeks big

    :param stat_per_game: List of stats
    :return: Updated list, if applicable
    """
    if len(stat_per_game) != 16:
        stat_per_game.append("0")

if __name__ == "__main__": 
    res = get_stats()
    soup = BeautifulSoup(res, "html.parser")
    game_stats = soup.find_all("tr", id=lambda x: x and x.startswith("stats."))
    rec = get_stat_for_season(game_stats, "rec")
    print(sum([int(n) for n in rec]))