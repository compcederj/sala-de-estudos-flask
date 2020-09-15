from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.lessons import Lesson


class LessonsDAO:

    @staticmethod
    def list_lessons_by_subject(subject_id):
        lessons = (db.session.query(Lesson.id, Lesson.title, Lesson.lesson_index, Lesson.lesson_index)
                   .filter(Lesson.subject_id == subject_id)
                   .all())

        lessons = [
            {
                "id": lesson[0],
                "title": lesson[1],
                "lesson_index": lesson[2],
                "thumbnail": lesson[3]
            }
            for lesson in lessons
        ]

        return lessons
