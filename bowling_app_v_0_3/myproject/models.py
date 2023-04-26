from myproject import db

class Games(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Text)
    game_1 = db.Column(db.Integer)
    game_2 = db.Column(db.Integer)
    game_3 = db.Column(db.Integer)
    avg_game = db.Column(db.Integer)
    series = db.Column(db.Integer)

    def __init__(self, name, date, game_1, game_2, game_3, avg_game, series):
        self.name = name
        self.date = date
        self.game_1 = game_1
        self.game_2 = game_2
        self.game_3 = game_3
        self.avg_game = avg_game
        self.series = series

    def __repr__(self):
        return f'On {self.date}, {self.name} scored {self.game_1}, {self.game_2}, and {self.game_3}. ' \
               f'Game series: {self.series}. Game average: {self.avg_game}.'
