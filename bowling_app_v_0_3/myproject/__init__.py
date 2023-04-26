import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#######################
## data base section ##
#######################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

#########################
## register blueprints ##
#########################

from myproject.game.views import game_blueprints
from myproject.bowlers.views import bowlers_blueprints

app.register_blueprint(game_blueprints, url_prefix='/game')
app.register_blueprint(bowlers_blueprints, url_prefix='/bowlers')
