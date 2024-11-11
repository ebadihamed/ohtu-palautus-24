import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists


    def __str__(self):
        return f"{self.name:20} {self.team:10} {self.goals:3} + {self.assists:3} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        return requests.get(self.url).json()

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        self.player = []

        def is_finnish(n):
            return n['nationality'] == nationality
    
        fin_players = filter(is_finnish, self.players)
        for player_dict in fin_players:
            p = Player(player_dict)
            self.player.append(p)
        
        return sorted(self.player, key=lambda x: x.points, reverse=True)
