import click

from sala_de_estudos_flask.ext.db import db


def create_db():
    """ Creates database structure """
    try:
        db.create_all()
        click.echo("Database creation was succeed.")
    except Exception as err:
        click.echo("It was not possible to create database.")
        click.echo(str(err))


def drop_db():
    db.drop_all()
