from flask import Flask 
from flask_assets import Environment, Bundle

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.cache_control.public = True
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    r.cache_control.max_age = 0
    return r

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle('index.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

scss_team = Bundle('team.scss', filters='pyscss', output='team.css')
assets.register('scss_team', scss_team)

from app import routes

