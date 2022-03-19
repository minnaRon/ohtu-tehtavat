from datetime import datetime
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from ", players[0].nationality, datetime.now())

    for player in players:
        print(player)


main()
