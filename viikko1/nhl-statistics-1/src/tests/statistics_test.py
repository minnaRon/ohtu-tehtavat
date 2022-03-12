import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_right_player(self):
        #haku palauttaa pelaajan Kurri tiedot nimellä Kurri
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.goals, 37)

    def test_search_unknown_name_returns_none(self):
        #jos pelaajaa ei löydy palautuu None
        self.assertIsNone(self.statistics.search("noname"))

    def test_team_has_right_members(self):
        #tiimiin EDM tulee jäseniksi Semenko, Kurri ja Gretzky
        self.assertEqual(self.statistics.team("EDM")[0].name, "Semenko")
        self.assertEqual(self.statistics.team("EDM")[1].name, "Kurri")
        self.assertEqual(self.statistics.team("EDM")[2].name, "Gretzky")
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_unknown_team_returns_empty_list(self):
        #lista tyhjä jos parametrin tiimiä ei ole
        self.assertEqual(self.statistics.team("ABC"), [])

    def test_top_scored_fetches_right_amount_of_players(self):
        #järjestää pelaajat oikein pisteiden mukaan
        self.assertEqual(len(self.statistics.top_scorers(2)), 2)
