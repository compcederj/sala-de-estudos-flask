from flask import Flask, redirect

from sala_de_estudos_flask.ext import config


def create_app() -> Flask:
    app = Flask(__name__)
    config.init_app(app)

    @app.route("/")
    def home():
        return redirect("http://saladeestudos.esy.es")

    return app
