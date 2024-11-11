import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    def is_finnish(n):
        return n['nationality'] == 'FIN'
    
    fin_players = filter(is_finnish, response)

    for player_dict in fin_players:
        player = Player(player_dict)
        players.append(player)
        
    print("Players from FIN:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
