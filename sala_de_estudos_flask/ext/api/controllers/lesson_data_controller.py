from http.client import NOT_FOUND

from sala_de_estudos_flask.ext.api.controllers.controller import Controller
from sala_de_estudos_flask.ext.dao.lesson_data_dao import LessonDataDAO


class LessonDataController(Controller):
    def get(self, subject_id: int, lesson_id: int):
        lesson_data = LessonDataDAO().get_json(subject_id, lesson_id)

        if lesson_data:
            return self.as_json(lesson_data)

        return self.make_error(
            NOT_FOUND,
            "Not Found",
            f"It was not possible to find lesson data for subject_id {subject_id} and lesson_id {lesson_id}."
            "Try another subject_id and lesson_id."
        )
