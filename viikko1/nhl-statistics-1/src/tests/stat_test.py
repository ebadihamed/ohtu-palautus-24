import unittest
from statistics_service import StatisticsService, SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_found(self):
        player = self.stats.search("Kurri")
        print()
        self.assertAlmostEqual(str(player), "Kurri EDM 37 + 53 = 90")
    
    def test_search_not_found(self):
        player = self.stats.search("Messi")
        self.assertIsNone(player)

    def test_team(self):
       team = self.stats.team("PIT")
       self.assertEqual(str(team[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_points(self):
        top = self.stats.top(1)
        self.assertEqual(str(top[0]), "Gretzky EDM 35 + 89 = 124")
    
    def test_top_goals(self):
        top = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(top[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_assists(self):
        top = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(top[0]), "Gretzky EDM 35 + 89 = 124")
    
    