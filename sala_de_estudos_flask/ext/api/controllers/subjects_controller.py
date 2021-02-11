from http.client import NOT_FOUND

from sala_de_estudos_flask.ext.api.controllers.controller import Controller
from sala_de_estudos_flask.ext.dao.subject_dao import SubjectsDAO
from sala_de_estudos_flask.ext.models.subjects import SubjectTypeEnum


class SubjectsController(Controller):
    def __init__(self):
        super(SubjectsController, self).__init__()

    def list_all(self):
        subjects = SubjectsDAO().list_all()
        return self.as_json(subjects)

    def get(self, id_):
        subject = SubjectsDAO().get_by_id(id_)
        if subject:
            data = {
                "id": subject.id,
                "code": subject.code,
                "name": subject.name,
                "type": "OBRIGATÓRIA" if subject.type == SubjectTypeEnum.OBRIGATORIA else "OPTATIVA",
                "workload": subject.workload,
                "amount_lessons": subject.amount_lessons,
                "drive_link": subject.drive_link,
                "github_link": subject.github_link,
            }
            return self.as_json(data)
        else:
            return self.make_error(status_code=NOT_FOUND, status="Not Found", description="Subject was not found")

    def redirect_whatsapp(self, id_):
        whatsapp_link = SubjectsDAO.get_whatsapp_link_by_id(id_)
        if whatsapp_link:
            return self.redirect(whatsapp_link)
        else:
            return NOT_FOUND
