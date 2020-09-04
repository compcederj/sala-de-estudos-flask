from flask_admin.contrib.sqla import ModelView


class EvaluationsView(ModelView):
    """Evaluation admin interface"""
    name = "Avaliações"
    column_labels = {
        "evaluation_key": "Tipo de Avaliação",
        "subject": "Disciplina",
        "type": "Tipo",
        "year": "Ano",
        "semester": "Semestre",
        "download_link": "Link para download"
    }

    column_exclude_list = ["created_at", "updated_at"]
    form_excluded_columns = ["created_at", "updated_at"]


class EvaluationKeyView(ModelView):
    """EvaluationKey admin interface"""
    name = "Tipo de Avaliação"
    column_labels = {
        "description": "Tipo de avaliação"
    }

    column_exclude_list = ["created_at", "updated_at"]
    form_excluded_columns = ["created_at", "updated_at", "evaluation"]

