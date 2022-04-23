class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.even_score = {0:"Love-All", 1:"Fifteen-All", 2:"Thirty-All", 3:"Forty-All"}
        self.from_four_points_score = {1:"Advantage player1", -1:"Advantage player2"}
        self.temp_score = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.points += 1
        else:
            self.player2.points += 1

    def get_score(self):
        score = ""

        if self.player1.points == self.player2.points:
            score = self.points_even()

        elif self.player1.points >= 4 or self.player2.points >= 4:
            score = self.points_from_four()

        else:
            score = self.points_one_to_three()

        return score

    def points_even(self):
        return self.even_score[self.player1.points] if self.player1.points <= 3 else "Deuce"

    def points_from_four(self):
            minus_result = self.player1.points - self.player2.points
            score = self.from_four_points_score[minus_result] if -1 <= minus_result < 2 else "Win for player2"
            return score if minus_result < 2 else "Win for player1"

    def points_one_to_three(self):
        for i in range(1, 3):
            temp_points = self.player1.points if i == 1 else self.player2.points
            score = "" if i == 1 else score + "-"
            score += self.temp_score[temp_points]
        
        return score
