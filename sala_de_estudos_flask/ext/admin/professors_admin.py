from flask_admin.contrib.sqla import ModelView


class ProfessorsView(ModelView):
    """Professor admin interface"""
    name = "Professores"

    column_labels = {"name": "Nome"}
    column_list = ["name", "email", "site"]
    form_excluded_columns = ["created_at", "updated_at", "professor_subject", "professor_lesson"]
