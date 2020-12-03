from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models import LessonData, Lesson


class LessonDataDAO:
    @staticmethod
    def get_json(subject_id: int, lesson_id: int):
        lesson_data = (db.session.query(LessonData.json_xml, LessonData.json_index, LessonData.json_sync)
                       .join(Lesson)
                       .filter(Lesson.subject_id == subject_id)
                       .filter(LessonData.lesson_id == lesson_id)
                       .first())
        try:
            lesson_data = {
                "main": lesson_data[0],
                "index": lesson_data[1],
                "sync": lesson_data[2]
            }
        except IndexError:
            lesson_data = {}

        return lesson_data
