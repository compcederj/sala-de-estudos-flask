from flask import Flask

from sala_de_estudos_flask.ext import config


def create_app() -> Flask:
    app = Flask(__name__)
    config.init_app(app)

    return app
