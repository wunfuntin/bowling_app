from wtforms import Form, StringField, IntegerField, SubmitField, DateField


class AddGameForm(Form):
    name = StringField('Name of Bowler: ')
    date = DateField('Choose a date', format='%Y-%m-%d')
    game_1 = IntegerField('Game 1: ')
    game_2 = IntegerField('Game 2: ')
    game_3 = IntegerField('Game 3: ')
    submit = SubmitField('Submit Games')
