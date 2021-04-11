import os.path

from connexion import FlaskApp
from flask import Flask, redirect

from sala_de_estudos_flask.ext import config
from sala_de_estudos_flask.ext.api import add_apis


def create_app() -> Flask:
    basedir = os.path.abspath(os.path.dirname(__file__))
    connexion_app = FlaskApp(__name__, specification_dir=basedir)

    app = connexion_app.app
    config.init_app(app)

    add_apis(connexion_app)

    @app.route("/")
    def home():
        return redirect("http://saladeestudos.esy.es")

    return app
