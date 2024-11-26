from enum import Enum

class Scores(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3


class Score:
    def __init__(self, player1_score=0, player2_score=0):
        self.m_score1 = player1_score
        self.m_score2 = player2_score

    def update_scores(self, player1_score, player2_score):
        self.m_score1 = player1_score
        self.m_score2 = player2_score

    def tie(self):
        if self.m_score1 <= 2:
            return f"{Scores(self.m_score1).name}-All"
        return "Deuce"
    
    def advantage(self):
        score = ""
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def otherwise(self):
        score1 = Scores(self.m_score1).name
        score2 = Scores(self.m_score2).name
        return f"{score1}-{score2}"


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player_1 = player1_name
        self.player_2 = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = Score(self.m_score1, self.m_score2)


    def won_point(self, player_name):
        if player_name == self.player_1:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
        self.score.update_scores(self.m_score1, self.m_score2)


    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.score.tie()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.score.advantage() 
        else:
            return self.score.otherwise()