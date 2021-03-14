from flask import Blueprint

from sala_de_estudos_flask.ext.api.controllers.lesson_data_controller import LessonDataController
from sala_de_estudos_flask.ext.api.controllers.lessons_controller import LessonsController
from sala_de_estudos_flask.ext.api.controllers.subjects_controller import SubjectsController

bp = Blueprint("api", __name__)


@bp.route("/api/v1/subjects/")
def subjects_route():
    return SubjectsController().list_all()


@bp.route("/api/v1/subject/<int:id_>/")
def subject_route(id_: int):
    return SubjectsController().get(id_)


@bp.route("/api/v1/subject/<string:code>/code/")
def subject_code_route(code: str):
    return SubjectsController().get_by_code(code)


@bp.route("/redirect/subject/<int:id_>/whatsapp/")
def subject_whatsapp_route(id_: int):
    return SubjectsController().redirect_whatsapp(id_)


@bp.route("/api/v1/subject/<int:subject_id>/lessons/")
def lessons_route(subject_id):
    return LessonsController().list(subject_id)


@bp.route("/api/v1/subject/<int:subject_id>/lesson/<int:lesson_id>/")
def lesson_data_route(subject_id: int, lesson_id: int):
    return LessonDataController().get(subject_id, lesson_id)
