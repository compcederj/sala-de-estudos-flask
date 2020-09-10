from flask_admin.contrib.sqla import ModelView

from sala_de_estudos_flask.ext.models.lessons import ProfessorLesson


class LessonsView(ModelView):
    """Lessons admin interface"""
    inline_models = (ProfessorLesson,)
    column_labels = {
        "subject": "Disciplina",
        "lesson_index": "Aula número",
        "title": "Título da Aula",
        "length": "Duração",
    }

    column_exclude_list = ["created_at", "updated_at"]

    form_excluded_columns = ["created_at", "updated_at", "lesson", "professor_lesson"]
