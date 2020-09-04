from flask_admin.contrib.sqla import ModelView


class LessonsView(ModelView):
    """Lessons admin interface"""
    column_labels = {
        "subject": "Disciplina",
        "index": "Aula número",
        "title": "Título da Aula",
        "length": "Duração",
    }

    column_exclude_list = ["created_at", "updated_at"]

    form_excluded_columns = ["created_at", "updated_at", "lesson", "professor_lesson"]
