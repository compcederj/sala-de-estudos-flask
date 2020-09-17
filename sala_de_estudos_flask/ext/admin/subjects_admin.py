from flask_admin.contrib.sqla import ModelView

from sala_de_estudos_flask.ext.models.subjects import ProfessorSubject


class SubjectsView(ModelView):
    """Subjects admin interface"""
    column_labels = {
        "code": "Código da disciplina ead050XX",
        "type": "Tipo (obrigatória, optativa)",
        "workload": "Carga Horária",
        "professor_subject": "Professores responsável pela disciplina"
    }
    column_exclude_list = ["created_at", "updated_at"]

    form_excluded_columns = [
        "created_at",
        "updated_at",
        "lesson",
        "professor_subject",
        "professor_lesson",
        "evaluation"
    ]
