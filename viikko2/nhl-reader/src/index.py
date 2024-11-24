import requests
from player import Player, PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    read = PlayerReader(url).get_players()
    stats = PlayerStats(read)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()