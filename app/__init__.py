from flask import Flask 
from flask_assets import Environment, Bundle

app = Flask(__name__) 
assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle('index.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

scss_team = Bundle('team.scss', filters='pyscss', output='team.css')
assets.register('scss_team', scss_team)

from app import routes

