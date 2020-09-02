from flask_admin.contrib.sqla import ModelView

from sala_de_estudos_flask.ext.models import ProfessorSubject


class SubjectsView(ModelView):
    """Subjects admin interface"""
    inline_models = (ProfessorSubject,)
