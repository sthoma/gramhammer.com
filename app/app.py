import os

from flask import Flask
from extensions import db, assets
from extensions import js_libs, js_main, less
from blueprints.about import about
from blueprints.accounts import accounts
from blueprints.api import api

## App ##
app = Flask(__name__, static_folder='static',
            template_folder='templates')

## Config ##
flask_env = os.environ.get('FLASK_ENV')

if flask_env is None:
    app.config.from_object('app.config.DevelopmentConfig')
else:
    app.config.from_pyfile('app.config.%sConfig') % flask_env

## Database ##
db.init_app(app)
db.app = app

## Assets ##
assets.init_app(app)
assets.register('js_libs', js_libs)
assets.register('js_main', js_main)
assets.register('css_main', less)

## Blueprints ##
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(api, url_prefix='/api')
