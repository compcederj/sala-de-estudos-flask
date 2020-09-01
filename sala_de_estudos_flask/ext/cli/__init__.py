
from flask import Flask

from sala_de_estudos_flask.ext.db.commands import create_db


def init_app(app: Flask):

    @app.cli.command()
    def create_database():
        """ Creates database """
        create_db()
