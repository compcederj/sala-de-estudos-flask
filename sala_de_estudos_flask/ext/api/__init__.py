from os.path import abspath, dirname, join

from connexion import FlaskApp
from flask import Flask
from flask_cors import CORS

from sala_de_estudos_flask.ext.api.routes import bp


def init_app(app: Flask):
    app.register_blueprint(bp)
    CORS(app)


def add_apis(app: FlaskApp):
    basedir = abspath(dirname(__file__))
    app.add_api(join(basedir, "routes.yaml"))
