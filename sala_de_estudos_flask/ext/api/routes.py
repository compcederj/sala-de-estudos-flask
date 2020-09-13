from flask import Blueprint

from sala_de_estudos_flask.ext.api.controllers.subjects_controller import SubjectsController


bp = Blueprint("api", __name__)


@bp.route("/api/v1/subjects/")
def subjects_route():
    return SubjectsController().list_all()


@bp.route("/api/v1/subject/<int:id_>/")
def subject_route(id_: int):
    return SubjectsController().get(id_)


@bp.route("/redirect/subject/<int:id_>/whatsapp/")
def subject_whatsapp_route(id_: int):
    return SubjectsController().redirect_whatsapp(id_)
