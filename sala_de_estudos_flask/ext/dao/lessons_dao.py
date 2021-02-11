from typing import Dict, List, Union

from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.lessons import Lesson


class LessonsDAO:
    @staticmethod
    def list_lessons_by_subject(subject_id) -> List[Dict[str, Union[int, str]]]:
        lessons = (
            db.session.query(Lesson.id, Lesson.title, Lesson.lesson_index, Lesson.thumbnail)
            .filter(Lesson.subject_id == subject_id)
            .all()
        )

        lessons = [
            {"id": lesson[0], "title": lesson[1], "lesson_index": lesson[2], "thumbnail": lesson[3]}
            for lesson in lessons
        ]

        return lessons
