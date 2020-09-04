from flask_admin.contrib.sqla import ModelView

# from sala_de_estudos_flask.ext.models import ProfessorSubject
from sala_de_estudos_flask.ext.models.subjects import ProfessorSubject


class SubjectsView(ModelView):
    """Subjects admin interface"""
    inline_models = (ProfessorSubject,)
    column_labels = {
        "code": "Código da disciplina ead050XX",
        "type": "Tipo (obrigatória, optativa)",
        "workload": "Carga Horária",
    }
    column_exclude_list = ["created_at", "updated_at"]

    form_excluded_columns = ["created_at", "updated_at", "lesson", "professor_lesson"]
