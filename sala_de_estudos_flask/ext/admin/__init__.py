from flask import Flask
from flask_admin import Admin

from sala_de_estudos_flask.ext.admin.professors_admin import ProfessorsView
from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models import Professor

admin = Admin()


def init_app(app: Flask):
    admin.name = app.config["ADMIN_NAME"]
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.url = "/admin"

    admin.add_view(ProfessorsView(Professor, db.session))
