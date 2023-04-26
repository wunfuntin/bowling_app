from flask import Blueprint, render_template, url_for, request, redirect
from myproject import db
import pandas as pd
import sqlite3
import json
import plotly
import plotly.express as px


bowlers_blueprints = Blueprint('bowlers', __name__,
                               template_folder='templates/bowlers')


@bowlers_blueprints.route('/<name>', methods=['GET', 'POST'])
def bowler(name):
    # capitalize the name to search the db
    bowler_name = name.capitalize()

    # create connection to database using the full address because the db is in different directory
    connection = sqlite3.connect(
        r'/Users/rwalker/PycharmProjects/bowling_project/bowling_app_v_0_3/myproject/data.sqlite')
    # select the appropriate table from the db
    df = pd.read_sql_query("SELECT * FROM games", con=connection)
    # commit and close the db connection
    connection.commit()
    connection.close()
    # print(df)
    # create new df using the bowler we are going to display
    result_df = df[df['name'] == bowler_name]
    # print(result_df)
    pd.to_datetime(result_df['date'])
    # create figures of the bowling data
    fig1 = px.scatter(data_frame=result_df, x='date', y='avg_game', color='avg_game', size='avg_game')

    fig2 = px.bar(data_frame=result_df, x='date', y=['game_1', 'game_2', 'game_3'])

    # update the width between bars
    fig2.update_layout(bargap=0.9)

    graph_json1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    graph_json2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # game max averages and overall average
    game_1_avg = result_df['game_1'].mean().round(0)
    game_1_max = result_df['game_1'].max()
    game_2_avg = result_df['game_2'].mean().round(0)
    game_2_max = result_df['game_2'].max()
    game_3_avg = result_df['game_3'].mean().round(0)
    game_3_max = result_df['game_3'].max()
    game_avg = result_df['avg_game'].mean().round(0)

    return render_template('bowler.html',
                           name=name,
                           graph_json1=graph_json1,
                           graph_json2=graph_json2,
                           game_1_avg=game_1_avg,
                           game_1_max=game_1_max,
                           game_2_avg=game_2_avg,
                           game_2_max=game_2_max,
                           game_3_avg=game_3_avg,
                           game_3_max=game_3_max,
                           game_avg=game_avg)
