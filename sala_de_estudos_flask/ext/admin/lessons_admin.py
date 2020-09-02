from flask_admin.contrib.sqla import ModelView

from sala_de_estudos_flask.ext.models import ProfessorLesson


class LessonsView(ModelView):
    """Lessons admin interface"""
    inline_models = (ProfessorLesson,)
