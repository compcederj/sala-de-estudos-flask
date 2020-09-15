from sala_de_estudos_flask.ext.dao.lessons_dao import LessonsDAO


class LessonsController:
    @staticmethod
    def list(subject_id):
        lessons = LessonsDAO.list_lessons_by_subject(subject_id)
