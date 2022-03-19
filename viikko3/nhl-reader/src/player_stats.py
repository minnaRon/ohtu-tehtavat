class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str) ->list:
        
        players = []        
        for player in self._players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda player : player.goals + player.assists, reverse=True)

        return players
