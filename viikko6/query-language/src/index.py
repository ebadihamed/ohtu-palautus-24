from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import All, And, Or, HasAtLeast, PlaysIn, Not, HasFewerThan

class QueryBuilder:
    def __init__(self, build = All()):
        self.build_stack = build

    def plays_in(self, team):
        return QueryBuilder(And(self.build_stack, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.build_stack, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.build_stack, HasFewerThan(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.build_stack
    
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()

    matcher1 = (
    query
    .plays_in("PHI")
    .has_at_least(10, "assists")
    .has_fewer_than(10, "goals")
    .build()
    )

    matcher2 = (
    query
        .plays_in("EDM")
        .has_at_least(50, "points")
        .build()
    )

    matcher = query.one_of(matcher1, matcher2).build()

    for player in stats.matches(matcher):
        print(player)

    
if __name__ == "__main__":
    main()


