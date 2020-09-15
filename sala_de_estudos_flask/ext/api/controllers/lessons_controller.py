from http.client import NOT_FOUND

from sala_de_estudos_flask.ext.api.controllers import Controller
from sala_de_estudos_flask.ext.dao.lessons_dao import LessonsDAO


class LessonsController(Controller):

    def list(self, subject_id):
        lessons = LessonsDAO.list_lessons_by_subject(subject_id)

        if lessons:
            return self.as_json(lessons)

        return self.make_error(
            NOT_FOUND,
            "Not Found",
            "It was not found lessons for this subject. "
            "Try another subject."
        )
