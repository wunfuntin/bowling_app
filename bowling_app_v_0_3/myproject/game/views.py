from flask import Blueprint, render_template, url_for, request, redirect
from myproject import db
from myproject.models import Games
from myproject.game.forms import AddGameForm
import pandas as pd
import sqlite3

game_blueprints = Blueprint('game', __name__,
                               template_folder='templates/game')

@game_blueprints.route('/add', methods=['GET', 'POST'])
def add():
    form = AddGameForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        date = form.date.data
        game_1 = form.game_1.data
        game_2 = form.game_2.data
        game_3 = form.game_3.data
        series = game_1 + game_2 + game_3
        avg_game = (series / 3).__round__(1)
        new_bowler = Games(name, date, game_1, game_2, game_3, avg_game, series)
        db.session.add(new_bowler)
        db.session.commit()

        return redirect(url_for('game.list_games'))
    return render_template('add.html', form=form)

@game_blueprints.route('/list')
def list_games():
    games = Games.query.all()
    connection = sqlite3.connect(r'/Users/rwalker/PycharmProjects/bowling_project/bowling_app_v_0_3/myproject/data.sqlite')
    df = pd.read_sql_query("SELECT * FROM games", con=connection)
    print(df)
    connection.commit()
    connection.close()
    # print(type(games))  # class list
    # print(games)  # [Ryan scored 186, 200, and 183]
    # for game in games:
    # print(game)  # Ryan scored 186, 200, and 183
    return render_template('list.html', games=games)

@game_blueprints.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    form = AddGameForm(request.form)
    game_to_update = Games.query.get_or_404(id)
    if request.method == 'POST':
        game_to_update.name = request.form['name']
        game_to_update.date = request.form['date']
        game_to_update.game_1 = request.form['game_1']
        game_to_update.game_2 = request.form['game_2']
        game_to_update.game_3 = request.form['game_3']
        game_to_update.series = int(game_to_update.game_1) + int(game_to_update.game_2) + int(game_to_update.game_3)
        game_to_update.avg_game = (int(game_to_update.series) / 3).__round__(1)
        db.session.commit()

        return redirect(url_for('game.list_games'))
    return render_template('update.html', form=form, game_to_update=game_to_update)