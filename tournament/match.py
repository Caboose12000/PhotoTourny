class Match:
    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2
        self.winner = None

    def set_winner(self, winner):
        if winner in (self.image1, self.image2):
            self.winner = winner
        else:
            raise ValueError("Winner must be one of the match participants")

    def get_winner(self):
        return self.winner