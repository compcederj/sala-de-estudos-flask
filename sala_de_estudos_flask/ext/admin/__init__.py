from flask import Flask
from flask_admin import Admin

from sala_de_estudos_flask.ext.admin.evaluations_view import EvaluationsView, EvaluationKeyView
from sala_de_estudos_flask.ext.admin.lessons_admin import LessonsView
from sala_de_estudos_flask.ext.admin.professors_admin import ProfessorsView
from sala_de_estudos_flask.ext.admin.subjects_admin import SubjectsView
from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.evaluations import Evaluation, EvaluationKey
from sala_de_estudos_flask.ext.models.lessons import Lesson
from sala_de_estudos_flask.ext.models.professors import Professor
from sala_de_estudos_flask.ext.models.subjects import Subject

admin = Admin()


def init_app(app: Flask):
    admin.name = app.config["ADMIN_NAME"]
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.url = "/admin"

    admin.add_view(ProfessorsView(Professor, db.session, "Professores"))

    admin.add_view(SubjectsView(Subject, db.session, "Disciplinas"))

    admin.add_view(LessonsView(Lesson, db.session, "Aulas"))

    admin.add_view(EvaluationsView(Evaluation, db.session, "Avaliações", category="Avaliações"))
    admin.add_view(EvaluationKeyView(EvaluationKey, db.session, "Tipo de Avaliação", category="Avaliações"))
